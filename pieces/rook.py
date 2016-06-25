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
from setup.algebraic_notation import algebraic, notation_const
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

        def shift(location, direction):
            """
            Shifts location given direction
            :type location algebraic.Location
            :type direction int
            :return:
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
        current = shift(self.location, direction)

        while current.exit == 0 and position.is_square_empty(current):
            possible.append(algebraic.Move.init_loc(current, self, notation_const.MOVEMENT))
            current = shift(current, direction)

        return possible

    def possible_moves(self, location, position):
        """
        Returns all possible rook moves.
        :type location: algebraic.Location
        :param position: board.Board
        """
        moves = []
        moves.extend(self.direction_moves(0, position))
        moves.extend(self.direction_moves(1, position))
        moves.extend(self.direction_moves(2, position))
        moves.extend(self.direction_moves(3, position))

        return moves
