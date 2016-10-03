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

from chess_py.core.algebraic import notation_const
from chess_py.core.algebraic.location import Location
from chess_py.pieces.piece import Piece
from chess_py.pieces.rook import Rook

from chess_py.core.algebraic.move import Move


class King(Piece):
    def __init__(self, input_color, location):
        """
        Creates a King.

        :type input_color: Color
        :type location: Location
        """
        self.has_moved = False
        super(King, self).__init__(input_color, location, "♚", "♔")

    def __str__(self):
        return "K"

    def possible_moves(self, position):
        """
        Generates list of possible moves

        :type position: Board
        :rtype: list
        """
        moves = []

        def in_check_as_result(pos, move):
            """

            :type pos: Board
            :type move: Move
            """
            test = pos.copy()

            test.update(move)
            test_king = test.piece_at_square(move.end_loc)

            if not test_king.in_check(test):
                return True

            return False


        def add(function):
            if function(self.location).on_board():

                move = Move(end_loc=function(self.location),
                            piece=self,
                            status=notation_const.MOVEMENT,
                            start_rank=self.location.rank,
                            start_file=self.location.file)

                if position.is_square_empty(function(self.location)) and in_check_as_result(position, move):
                    move.status = notation_const.MOVEMENT
                    moves.append(move)


                else:
                    move.status = notation_const.CAPTURE

                    if position.piece_at_square(function(self.location)).color != self.color and \
                        type(position.piece_at_square(function(self.location))) is not King and \
                        not in_check_as_result(position, move):
                        moves.append(move)

        def add_castle():
            """
            Adds kingside and queenside
            """
            if not self.in_check(position) and not self.has_moved:

                # King side castle
                rook = position.piece_at_square(Location(self.location.rank, 7))
                # If both the king and rook are in the right place and neither have moved
                if rook is not None and type(rook) is Rook and not rook.has_moved:
                    # If it is kingside castle and both spaces are empty
                    if position.is_square_empty(self.location.shift_right()) and \
                            position.is_square_empty(self.location.shift_right().shift_right()):

                        test = position.copy()
                        test.move_piece(self.location, self.location.shift_right())

                        # Cannot castle if in check after moving one square to the right
                        if test.piece_at_square(self.location.shift_right().in_check()):
                            return

                        test.move_piece(self.location.shift_right(), self.location.shift_right().shift_right())

                        # Cannot castle if in check after moving one more square to the right
                        if test.piece_at_square(self.location.shift_right().shift_right().in_check()):
                            return

                        moves.append(Move(end_loc=self.location.shift_right().shift_right(),
                                          piece=self,
                                          status=notation_const.KING_SIDE_CASTLE,
                                          start_rank=self.location.rank,
                                          start_file=self.location.file))

                # Queen side castle
                rook = position.piece_at_square(Location(self.location.rank, 0))
                # If both the king and rook are in the right place and neither have moved
                if rook is not None and type(rook) is Rook and not rook.has_moved:

                    # If it is queen side castle and all intermediate squares are empty
                    if position.is_square_empty(self.location.shift_left()) and \
                        position.is_square_empty(self.location.shift_left().shift_left()) and \
                        position.is_square_empty(self.location.shift_left().shift_left().shift_left()):

                            test = position.copy()
                            test.move_piece(self.location, self.location.shift_left())

                            if test.piece_at_square(self.location.shift_left().in_check()):
                                return

                            test.move_piece(self.location, self.location.shift_left().shift_left())

                            if test.piece_at_square(self.location.shift_left().shift_left().in_check()):
                                return

                            moves.append(Move(end_loc=self.location.shift_left().shift_left(),
                                              piece=self,
                                              status=notation_const.QUEEN_SIDE_CASTLE,
                                              start_rank=self.location.rank,
                                              start_file=self.location.file))

        add(lambda x: x.shift_up())
        add(lambda x: x.shift_up_right())
        add(lambda x: x.shift_up_left())
        add(lambda x: x.shift_right())
        add(lambda x: x.shift_down())
        add(lambda x: x.shift_down_right())
        add(lambda x: x.shift_down_left())
        add(lambda x: x.shift_left())
        add_castle()

        return moves

    def in_check(self, position):
        """
        Finds if the king is in check

        :type position: Board
        :return: bool
        """
        # Loops through columns
        for row in position.position:

            # Loops through rows
            for piece in row:

                if piece is not None and piece.color != self.color:

                    for move in piece.possible_moves(position):

                        if move.end_loc == self.location:
                            return True

            return False
