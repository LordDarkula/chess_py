
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
import copy

from pieces.piece import Piece
from core.algebraic.move import Move
from core.algebraic import notation_const


class King(Piece):
    def __init__(self, input_color, location):
        super(King, self).__init__(input_color, location, "♚", "♔")

    def unfiltered(self, position):
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

        super(King, self).set_loc(moves)

        return moves

    def possible_moves(self, position):
        """

        :type position Board
        :return:
        """
        unfiltered = self.unfiltered(position)
        filtered = []

        for move in unfiltered:
            test = copy.deepcopy(unfiltered)
            test.update(move)
            if test.find_king(self.color) is not None:
                filtered.append(move)

        return filtered
