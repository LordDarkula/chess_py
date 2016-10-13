# -*- coding: utf-8 -*-

"""
Class stores Rook on the board

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

from chess_py.core.algebraic import notation_const
from chess_py.core.algebraic.location import Location
from chess_py.pieces.piece import Piece

from chess_py.core.algebraic.move import Move


class Rook(Piece):
    def __init__(self, input_color, location):
        """
        Initializes a rook that is capable of being compared to another rook,
        and returning a list of possible moves.

        :type input_color: Color
        :type location: Location
        """
        self.has_moved = False
        super(Rook, self).__init__(input_color, location, "♜", "♖")

    def __str__(self):
        return "R"

    def direction_moves(self, direction, position):
        """
        Finds moves in a given direction

        :type direction: lambda
        :type position: Board
        :rtype: list
        """
        possible = []
        current = direction(self.location)

        def side_move(status):
            return Move(end_loc=current,
                        piece=self,
                        status=status,
                        start_rank=self.location.rank,
                        start_file=self.location.file)

        assert isinstance(current, Location)
        while current.on_board() and \
                position.is_square_empty(current):
            possible.append(side_move(notation_const.MOVEMENT))

            current = direction(current)

        if self.contains_opposite_color_piece(current, position):
                possible.append(side_move(notation_const.CAPTURE))

        return possible

    def possible_moves(self, position):
        """
        Returns all possible rook moves.

        :type position: Board
        :rtype: list
        """
        moves = []

        for fn in self.list_of_func:
            if self.direction_moves(fn, position) is not None:
                moves.extend(self.direction_moves(fn, position))

        return moves
