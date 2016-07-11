# -*- coding: utf-8 -*-

"""
Class stores King on the board

rank
7 8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
6 7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
5 6 ║… … … … … … … …
4 5 ║… … … … … … … …
3 4 ║… … … … … … … …
2 3 ║… … … … … … … …
1 2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
0 1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
----╚═══════════════
——---a b c d e f g h
-----0 1 2 3 4 5 6 7
------file

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""
import copy

from chess_py.core import color
from chess_py.core.algebraic import notation_const
from chess_py.core.algebraic.location import Location
from chess_py.pieces.piece import Piece
from chess_py.pieces.rook import Rook

from chess_py.core.algebraic.move import Move


class King(Piece):
    def __init__(self, input_color, location):
        """
        Creates a King.
        :type input_color Color
        :type location Location
        """
        self.has_moved = False
        super(King, self).__init__(input_color, location, "♚", "♔")

    def unfiltered(self, position):
        """
        Generates list of possible moves
        :type position Board
        :rtype list
        """
        moves = []

        def add(function):
            if function(self.location).exit == 0:
                if position.is_square_empty(function(self.location)):
                    moves.append(Move(function(self.location), self, notation_const.MOVEMENT))

                elif not position.piece_at_square(function(self.location)).color.equals(self.color):
                    moves.append(Move(function(self.location), self, notation_const.CAPTURE))

        add(lambda x: x.shift_up())
        add(lambda x: x.shift_up_right())
        add(lambda x: x.shift_up_left())
        add(lambda x: x.shift_right())
        add(lambda x: x.shift_down())
        add(lambda x: x.shift_down_right())
        add(lambda x: x.shift_down_left())
        add(lambda x: x.shift_left())

        def edge_rank():
            if self.color.equals(color.white):
                return 0
            return 7

        def add_castle(direction, status, rook_file):
            """
            Adds kingside and queenside
            :type direction def
            :type status int
            :type rook_file int
            :rtype list
            """
            if position.piece_at_square(Location(edge_rank(), rook_file)) is not None and type(
                    position.piece_at_square(Location(edge_rank(), rook_file))) is Rook and not \
                    position.piece_at_square(Location(edge_rank(), rook_file)).has_moved:

                test = copy.deepcopy(position)
                test_king_loc = test.find_king(self.color)

                if test.is_square_empty(direction(test_king_loc)) and test.is_square_empty(
                        direction(direction(test_king_loc))):

                    test.move_piece(test_king_loc, direction(test_king_loc))

                    if not test.get_king(self.color).in_check(position):
                        moves.append(Move(direction(direction(Location(edge_rank(), self.location.file))),
                                          piece=self, status=status, start_rank=self.location.rank,
                                          start_file=self.location.file))

        if not self.has_moved:
            add_castle(lambda x: x.shift_right(), notation_const.KING_SIDE_CASTLE, 7)
            add_castle(lambda x: x.shift_left(), notation_const.QUEEN_SIDE_CASTLE, 0)

        super(King, self).set_loc(moves)

        return moves

    def enemy_moves(self, position):
        moves = []

        # Loops through columns
        for row in position.position:

            # Loops through rows
            for piece in row:

                # Tests if square on the board is not empty
                if piece is not None and type(piece) is not King and \
                        not piece.color.equals(self.color):

                    # Adds all of piece's possible moves to moves list.
                    moves.extend(piece.possible_moves(position))

        return moves

    def in_check(self, position):
        """
        Finds if the king is in check
        :type position Board
        :return:
        """
        for enemy_move in self.enemy_moves(position):

            if enemy_move.end_location().equals(self.location):
                return True
        return False

    def possible_moves(self, position):
        """
        Filters unfiltered moves so King cannot walk into check.
        :type position Board
        :rtype list
        """
        unfiltered = self.unfiltered(position)
        filtered = []

        for move in unfiltered:
            test = copy.deepcopy(position)

            test_move = Move(location=move.end_location(), piece=test.piece_at_square(Location(self.location.rank, self.location.file)),
                             status=move.status, start_rank=self.location.rank, start_file=self.location.file)

            test.update(test_move)


            test_king = test.piece_at_square(move.end_location())

            if not test_king.in_check(test):
                filtered.append(move)

        return filtered
