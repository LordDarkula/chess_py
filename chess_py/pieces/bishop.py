# -*- coding: utf-8 -*-

"""
Class stores Bishop on the board

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


class Bishop(Rook, Piece):
    def __init__(self, input_color, location):
        """
        Creates Bishop object that can be compared to and return possible moves

        :type: input_color: Color
        """
        Piece.__init__(self, input_color, location, "♝", "♗")

    def __str__(self):
        return "B"

    def possible_moves(self, position):
        """
        Returns all possible bishop moves.

        :type: position: Board
        :rtype: list
        """

        for move in itertools.chain(*[self.moves_in_direction(fn, position) for fn in self.diag_fn]):
            yield move
