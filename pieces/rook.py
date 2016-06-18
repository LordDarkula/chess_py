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
from setup.algebraic_notation import algebraic, special_notation_constants


class Rook:
    def __init__(self, input_color, location):
        """
        Initializes a rook that is capable of being compared to another rook,
        and returning a list of possible moves.
        :type input_color color.Color
        """
        self.color = input_color.color

        if self.color == color.white:
            self.symbol = "♜"
        else:
            self.symbol = "♖"

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces *
        """
        return type(piece) is type(self) and piece.color == self.color

    def possible_up_moves(self, location, position):
        """
        Returns possible moves north of the rook.
        :type location: algebraic.Location
        :type position: board.Board
        """
        possible = []

        default = location.shift_up()
        while location.not_none() and position.is_square_empty(default):
            possible.append(algebraic.Move.init_with_location(default, self, special_notation_constants.MOVEMENT))
            default = default.shift_up()

        if default.not_none() and position.piece_at_square(default).color != self.color:
            possible.append(algebraic.Move.init_with_location(default, self, special_notation_constants.CAPTURE))

        return possible

    def possible_down_moves(self, location, position):
        """
        Returns possible moves south of the rook.
        :type location: algebraic.Location
        :type position: board.Board
        """
        possible = []

        default = location.shift_down()
        while location.not_none() and position.is_square_empty(default):
            possible.append(algebraic.Move.init_with_location(default, self, special_notation_constants.MOVEMENT))
            default = default.shift_down()

        if default.not_none() and position.piece_at_square(default).color != self.color:
            possible.append(algebraic.Move.init_with_location(default, self, special_notation_constants.CAPTURE))

        return possible

    def possible_right_moves(self, location, position):
        """
        Returns possible moves east of the rook.
        :type location: algebraic.Location
        :type position: board.Board
        """
        possible = []

        default = location.shift_right()
        while location.not_none() and position.is_square_empty(default):
            possible.append(algebraic.Move.init_with_location(default, self, special_notation_constants.MOVEMENT))
            default = default.shift_right()

        if default.not_none() and position.piece_at_square(default).color != self.color:
            possible.append(algebraic.Move.init_with_location(default, self, special_notation_constants.CAPTURE))

        return possible

    def possible_left_moves(self, location, position):
        """
        Returns possible moves west of the rook.
        :type location: algebraic.Location
        :type position: board.Board
        """
        possible = []

        default = location.shift_left()
        while location.not_none() and position.is_square_empty(default):
            possible.append(algebraic.Move.init_with_location(default, self, special_notation_constants.MOVEMENT))
            default = default.shift_left()

        if default.not_none() and position.piece_at_square(default).color != self.color:
            possible.append(algebraic.Move.init_with_location(default, self, special_notation_constants.CAPTURE))

        return possible

    def possible_moves(self, location, position):
        """
        Returns all possible rook moves.
        :type location: algebraic.Location
        :param position: board.Board
        """
        moves = []
        moves.extend(self.possible_up_moves(location, position))
        moves.extend(self.possible_down_moves(location, position))
        moves.extend(self.possible_right_moves(location, position))
        moves.extend(self.possible_left_moves(location, position))
        return moves
