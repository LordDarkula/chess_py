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

from .piece import Piece
from .rook import Rook
from .bishop import Bishop


class Queen(Piece):
    def __init__(self, input_color, location):
        super(Queen, self).__init__(input_color, location, "♛", "♕")
        self.rook = Rook(input_color, location)
        self.bishop = Bishop(input_color, location)

    def __str__(self):
        return "Q"

    def possible_moves(self, position):
        self.rook = Rook(self.color, self.location)
        self.bishop = Bishop(self.color, self.location)

        moves = self.rook.possible_moves(position)
        moves.extend(self.bishop.possible_moves(position))

        for move in moves:
            move.piece = self

        return moves

