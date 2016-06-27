
"""

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
from pieces.piece import Piece
from pieces.rook import Rook
from setup.color import Color
from setup.board import Board


class Bishop(Piece, Rook):
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
        moves = []
        moves.extend(self.direction_moves(lambda x: x.shift_up_right(), position))
        moves.extend(self.direction_moves(lambda x: x.shift_up_left(), position))
        moves.extend(self.direction_moves(lambda x: x.shift_down_right(), position))
        moves.extend(self.direction_moves(lambda x: x.shift_down_left(), position))

        return moves
