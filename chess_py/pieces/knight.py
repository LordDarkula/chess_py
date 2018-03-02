# -*- coding: utf-8 -*-

"""
Class stores Knight on the board

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

from ..core.algebraic import notation_const
from ..pieces.piece import Piece
from ..core.algebraic.move import Move


class Knight(Piece):
    def __init__(self, input_color, location):
        """
        Initializes Knight
        :type: input_color: Color
        :type: location Location
        """
        super(Knight, self).__init__(input_color, location, "♞", "♘")

    def __str__(self):
        return "N"

    @staticmethod
    def _rotate_direction_ninety_degrees(direction):
        if direction == 3:
            return 0, 2
        right_angles = [direction - 1, direction + 1]
        for index, angle in enumerate(right_angles):
            if angle == -1:
                right_angles[index] = 3
            elif angle == 4:
                right_angles[index] = 0

        return right_angles

    def possible_moves(self, position):
        """
        Finds all possible knight moves
        :type: position Board
        :rtype: list
        """
        for direction in [0, 1, 2, 3]:
            angles = self._rotate_direction_ninety_degrees(direction)
            for angle in angles:
                try:
                    end_loc = self.location.shift(angle).shift(direction).shift(direction)
                    if position.is_square_empty(end_loc):
                        status = notation_const.MOVEMENT
                    elif not position.piece_at_square(end_loc).color == self.color:
                        status = notation_const.CAPTURE
                    else:
                        continue

                    yield Move(end_loc=end_loc,
                               piece=self,
                               status=status,
                               start_rank=self.location.rank,
                               start_file=self.location.file)

                except IndexError:
                    pass

