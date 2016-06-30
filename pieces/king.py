
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
from setup.algebraic.move import Move
from setup.algebraic import notation_const


class King(Piece):
    def __init__(self, input_color, location):
        super(King, self).__init__(input_color, location, "♚", "♔")

    def unfiltered(self, position):
        moves = []

        def add(function):
            if function(self.location).exit == 0:
                if position.is_square_empty(function(self.location)):
                    moves.append(Move(function(self.location), self, notation_const.MOVEMENT))

                elif position.piece_at_square(function(self.location)).color.equals(self.color):
                    moves.append(Move(function(self.location), self, notation_const.CAPTURE))

        add(lambda x: x.shift_up())
        add(lambda x: x.shift_right())
        add(lambda x: x.shift_down())
        add(lambda x: x.shift_left())

        super(King, self).possible_moves(moves)

        return moves
