# -*- coding: utf-8 -*-

"""
Class stores Queen on the board

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

import itertools

from .piece import Piece
from .rook import Rook
from .bishop import Bishop


class Queen(Bishop, Piece):
    def __init__(self, input_color, location):
        Piece.__init__(self, input_color, location, "♛", "♕")

    def __str__(self):
        return "Q"

    def possible_moves(self, position):
        for move in itertools.chain(Rook.possible_moves(self, position),
                                    Bishop.possible_moves(self, position)):
            yield move
