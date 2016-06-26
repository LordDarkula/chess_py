#TODO verify code and finalize class documentation

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

from setup import color
from setup.algebraic_notation.algebraic import Location, Move
from setup.algebraic_notation import notation_const
from pieces import piece


class Rook(piece.Piece):
    def __init__(self, input_color, location):
        """
        Initializes a rook that is capable of being compared to another rook,
        and returning a list of possible moves.
        :type input_color color.Color
        """

        super(Rook, self).__init__(input_color, location, "♜", "♖")

    def direction_moves(self, direction, position):
        """
        Finds moves in a given direction
        :type direction int
        :type position board.Board
        :rtype list
        """

        def shift(location):
            """
            Shifts location given direction
            :type location Location
            :rtype Location
            """
            if direction == 0:
                return location.shift_up
            elif direction == 1:
                return location.shift_left
            elif direction == 2:
                return location.shift_down
            elif direction == 3:
                return location.shift_right
            return location

        possible = []
        current = shift(self.location)

        while current.exit == 0 and position.is_square_empty(current):
            possible.append(Move.init_loc(current, self, notation_const.MOVEMENT))
            current = shift(current)

        current = shift(current)

        if current.exit == 0 and not position.piece_at_square(current).color.equals(self.color):
            possible.append(Move.init_loc(current, self, notation_const.CAPTURE))

        return possible

    def possible_moves(self, position):
        """
        Returns all possible rook moves.
        :param position: board.Board
        """
        moves = []
        moves.extend(self.direction_moves(0, position))
        moves.extend(self.direction_moves(1, position))
        moves.extend(self.direction_moves(2, position))
        moves.extend(self.direction_moves(3, position))

        return moves
