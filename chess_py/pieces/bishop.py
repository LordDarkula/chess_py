# -*- coding: utf-8 -*-

"""
Class stores Bishop on the board

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
from chess_py.pieces.piece import Piece
from chess_py.pieces.rook import Rook

from chess_py.core.color import Color


class Bishop(Piece):
    def __init__(self, input_color, location):
        """
        Creates Bishop object that can be compared to and return possible moves
        :type input_color: Color
        """
        super(Bishop, self).__init__(input_color, location, "♝", "♗")

    def possible_moves(self, position):
        """
        Returns all possible bishop moves.
        :type position Board
        :rtype list
        """
        rook = Rook(self.color, self.location)
        moves = []

        if rook.direction_moves(lambda x: x.shift_up_right(), position) is not None:
            moves.extend(rook.direction_moves(lambda x: x.shift_up_right(), position))

        if rook.direction_moves(lambda x: x.shift_up_left(), position) is not None:
            moves.extend(rook.direction_moves(lambda x: x.shift_up_left(), position))

        if rook.direction_moves(lambda x: x.shift_down_right(), position) is not None:
            moves.extend(rook.direction_moves(lambda x: x.shift_down_right(), position))

        if rook.direction_moves(lambda x: x.shift_down_left(), position) is not None:
            moves.extend(rook.direction_moves(lambda x: x.shift_down_left(), position))

        for move in moves:
            move.piece = self
            
        super(Bishop, self).set_loc(moves)

        return moves
