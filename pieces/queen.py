
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
from pieces import piece, rook, bishop
from setup import color


class Queen(piece.Piece, rook.Rook, bishop.Bishop):
    def __init__(self, input_color, location):
        super(Queen, self).__init__(input_color, location, "♛", "♕")

    def possible_moves(self, position):
        moves = super(Queen, self).possible_moves(position)
        moves.append(super(Queen, self).possible_moves(position))