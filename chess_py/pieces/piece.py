# -*- coding: utf-8 -*-

"""
Parent class for all pieces

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from abc import ABCMeta, abstractmethod

from ..core.algebraic.location import Location
from ..core import color
from ..core.color import Color


class Piece:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, input_color, location):
        """
        Initializes a piece that is capable of moving

        :type: input_color: Color
        :type: location: Location
        :type: white_symbol: str
        :type: black_symbol: str
        """
        assert isinstance(input_color, Color)
        assert isinstance(location, Location)

        self.color = input_color
        self.location = location

        self.cross_fn = [lambda x: x.shift_up(), lambda x: x.shift_right(),
                         lambda x: x.shift_down(), lambda x: x.shift_left()]

        self.diag_fn = [lambda x: x.shift_up_right(), lambda x: x.shift_up_left(),
                        lambda x: x.shift_down_right(), lambda x: x.shift_down_left()]

    def __key(self):
        return self.color, self.location

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        """
        Finds out if piece is the same type and color as self
        :type: other: Piece
        """
        return type(other) is type(self) and other.color == self.color

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "{}({}, {})".format(self.__class__, self.color, self.location)

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def _symbols(self):
        pass

    @abstractmethod
    def possible_moves(self, position):
        pass

    def __copy__(self):
        return self.__class__(self.color, self.location)

    @property
    def symbol(self):
        return self._symbols()[self.color]

    def contains_opposite_color_piece(self, square, position):
        """
        Finds if square on the board is occupied by a ``Piece``
        belonging to the opponent.

        :type: square: Location
        :type: position: Board
        :rtype: bool
        """
        return not position.is_square_empty(square) and \
            position.piece_at_square(square).color != self.color

    def create_move(self, end_loc, status):
        # TODO: fix circular imports
        from chess_py import Move
        return Move(end_loc=end_loc,
                    piece=self,
                    status=status,
                    start_loc=self.location)
