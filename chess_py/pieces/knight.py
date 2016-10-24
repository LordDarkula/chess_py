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

    def possible_moves(self, position):
        """
        Finds all possible knight moves
        :type: position Board
        :rtype: list
        """

        def cycle(index):
            """
            Cycles indexes containing shift directions perpendicular to current shift
            :type: index int
            :rtype tuple
            """
            if index == 0:
                return index + 1, index + 3

            elif index == 3:
                return index - 1, index - 3

            return index + 1, index - 1

        def dest(loc, function, ind):
            """
            Returns both destinations that result when the knight is moved two steps in
            one of the cardinal directions

            :type: loc: Location
            :type: function: def
            :type: ind: int
            :rtype: tuple
            """

            return self.cross_fn[cycle(ind)[0]](function(function(loc))), \
                   self.cross_fn[cycle(ind)[1]](function(function(loc)))

        moves = []

        for index, func in enumerate(self.cross_fn):
            dest_loc = dest(self.location, func, index)

            for j in range(2):

                if not dest_loc[j].on_board():
                    status = notation_const.NOT_IMPLEMENTED

                elif position.is_square_empty(dest_loc[j]):
                    status = notation_const.MOVEMENT

                elif not position.piece_at_square(dest_loc[j]).color == self.color:
                    status = notation_const.CAPTURE

                else:
                    status = notation_const.NOT_IMPLEMENTED

                if status != notation_const.NOT_IMPLEMENTED:
                    moves.append(Move(end_loc=dest_loc[j],
                                      piece=self,
                                      status=status,
                                      start_rank=self.location.rank,
                                      start_file=self.location.file))

        return moves
