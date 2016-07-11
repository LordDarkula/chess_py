# -*- coding: utf-8 -*-

"""
Class stores Rook on the board

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

from chess_py.core.algebraic import notation_const
from chess_py.core.algebraic.location import Location
from chess_py.pieces.piece import Piece

from chess_py.core.algebraic.move import Move


class Rook(Piece):
    def __init__(self, input_color, location):
        """
        Initializes a rook that is capable of being compared to another rook,
        and returning a list of possible moves.
        :type input_color color.Color
        """
        self.has_moved = False
        super(Rook, self).__init__(input_color, location, "♜", "♖")

    def direction_moves(self, direction, position):
        """
        Finds moves in a given direction
        :type direction lambda
        :type position board.Board
        :rtype list
        """
        possible = []
        current = direction(self.location)

        assert isinstance(current, Location)
        while current.exit == 0 and \
                position.is_square_empty(current):
            possible.append(Move(current, self, notation_const.MOVEMENT, start_rank=self.location.rank,
                                 start_file=self.location.file))
            current = direction(current)

        if current.exit == 0 and \
                not position.is_square_empty(current) and \
                not position.piece_at_square(current).color.equals(self.color):
                possible.append(Move(current, self, notation_const.CAPTURE, start_rank=self.location.rank,
                                     start_file=self.location.file))

        return possible

    def possible_moves(self, position):
        """
        Returns all possible rook moves.
        :type position Board
        :rtype list
        """
        moves = []

        if self.direction_moves(lambda x: x.shift_up(), position) is not None:
            moves.extend(self.direction_moves(lambda x: x.shift_up(), position))

        if self.direction_moves(lambda x: x.shift_right(), position) is not None:
            moves.extend(self.direction_moves(lambda x: x.shift_right(), position))

        if self.direction_moves(lambda x: x.shift_down(), position) is not None:
            moves.extend(self.direction_moves(lambda x: x.shift_down(), position))

        if self.direction_moves(lambda x: x.shift_left(), position) is not None:
            moves.extend(self.direction_moves(lambda x: x.shift_left(), position))
            
        super(Rook, self).set_loc(moves)

        return moves
