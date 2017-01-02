# -*- coding: utf-8 -*-

"""
Class stores King on the board

| rank
| 7 8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
| 6 7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
| 5 6 ║… … … … … … … …
| 4 5 ║… … … … … … … …
| 3 4 ║… … … … … … … …
| 2 3 ║… … … … … … … …
| 1 2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
| 0 1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
| ----╚═══════════════
| ——---a b c d e f g h
| -----0 1 2 3 4 5 6 7
| ------file

| Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from copy import copy

from .piece import Piece
from .rook import Rook
from ..core.algebraic import notation_const
from ..core.algebraic.location import Location
from ..core.algebraic.move import Move


class King(Piece):
    def __init__(self, input_color, location):
        """
        Creates a King.

        :type: input_color: Color
        :type: location: Location
        """
        super(King, self).__init__(input_color, location, "♚", "♔")
        self.has_moved = False
        self.cardinal_directions = self.cross_fn
        self.cardinal_directions.extend(self.diag_fn)

    def __str__(self):
        return "K"

    @staticmethod
    def in_check_as_result(pos, move):
        """
        Finds if playing my move would put this king
        in check.

        :type: pos: Board
        :type: move: Move
        :rtype: bool
        """
        test = copy(pos)
        test.update(move)
        test_king = test.get_king(move.color)

        return test_king.in_check(test)

    def add(self, function, position):
        if function(self.location).on_board():

            move = Move(end_loc=function(self.location),
                        piece=self,
                        status=notation_const.MOVEMENT,
                        start_rank=self.location.rank,
                        start_file=self.location.file)

            in_check_as_res = self.in_check_as_result(position, move)

            if position.is_square_empty(function(self.location)):
                if not in_check_as_res:
                    return [move]

                return []

            move.status = notation_const.CAPTURE

            if position.piece_at_square(function(self.location)).color != self.color and \
                            type(position.piece_at_square(function(self.location))) is not King and \
                    not in_check_as_res:
                return [move]

        return []

    def add_castle(self, position):
        """
        Adds kingside and queenside
        """
        moves = []
        if not self.in_check(position) and not self.has_moved:

            # King side castle
            rook = position.piece_at_square(Location(self.location.rank, 7))
            # If both the king and rook are in the right place and neither have moved
            if rook is not None and isinstance(rook, Rook) and not rook.has_moved:
                # If it is kingside castle and both spaces are empty
                if position.is_square_empty(self.location.shift_right()) and \
                        position.is_square_empty(self.location.shift_right().shift_right()):

                    test = copy(position)
                    test.move_piece(self.location, self.location.shift_right())

                    # Cannot castle if in check after moving one square to the right
                    if test.piece_at_square(self.location.shift_right()).in_check(position):
                        return

                    test.move_piece(self.location.shift_right(),
                                    self.location.shift_right().shift_right())

                    # Cannot castle if in check after moving one more square to the right
                    if test.piece_at_square(self.location.shift_right()
                                                    .shift_right()).in_check(position):
                        return

                    moves.append(Move(end_loc=self.location.shift_right().shift_right(),
                                      piece=self,
                                      status=notation_const.KING_SIDE_CASTLE,
                                      start_rank=self.location.rank,
                                      start_file=self.location.file))

            # Queen side castle
            rook = position.piece_at_square(Location(self.location.rank, 0))
            # If both the king and rook are in the right place and neither have moved
            if rook is not None and isinstance(rook, Rook) and not rook.has_moved:

                # If it is queen side castle and all intermediate squares are empty
                if position.is_square_empty(self.location.shift_left()) and \
                        position.is_square_empty(self.location.shift_left().shift_left()) and \
                        position.is_square_empty(self.location.shift_left()
                                                         .shift_left().shift_left()):

                    test = copy(position)
                    test.move_piece(self.location, self.location.shift_left())

                    if test.piece_at_square(self.location.shift_left()).in_check(position):
                        return

                    test.move_piece(self.location, self.location.shift_left().shift_left())

                    if test.piece_at_square(self.location.shift_left()
                                                    .shift_left()).in_check(position):
                        return

                    moves.append(Move(end_loc=self.location.shift_left().shift_left(),
                                      piece=self,
                                      status=notation_const.QUEEN_SIDE_CASTLE,
                                      start_rank=self.location.rank,
                                      start_file=self.location.file))

        return moves

    def possible_moves(self, position):
        """
        Generates list of possible moves

        :type: position: Board
        :rtype: list
        """
        moves = []

        for fn in self.cardinal_directions:
            moves.extend(self.add(fn, position))

        moves.extend(self.add_castle(position))

        return moves

    def in_check(self, position):
        """
        Finds if the king is in check

        :type: position: Board
        :return: bool
        """
        # Loops board
        for square in position:

            if square is not None and square.color != self.color:
                piece = square
                if isinstance(piece, King):
                    for fn in self.cross_fn:
                        if fn(self.location) == piece.location:
                            return True

                    for fn in self.diag_fn:
                        if fn(self.location) == piece.location:
                            return True

                    continue

                for move in piece.possible_moves(position):

                    if move.end_loc == self.location:
                        return True
        return False
