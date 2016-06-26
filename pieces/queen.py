
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
from pieces.bishop import Bishop


class Queen(Piece, Rook, Bishop):
    def __init__(self, input_color, location):
        super(Queen, self).__init__(input_color, location, "♛", "♕")
        self.rook = Rook(input_color, location)
        self.bishop = Bishop(input_color, location)

    def possible_moves(self, position):
        moves = self.rook.possible_moves(position)
        moves.append(self.bishop.possible_moves(position))