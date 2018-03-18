# -*- coding: utf-8 -*-

"""
Class that stores chess moves.
Destination, status and piece making move are required
to initialize Move.

:type: end_loc: Location
:type: piece: Piece
:type: status: int

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from .location import Location


class Move:
    def __init__(self,
                 end_loc,
                 piece,
                 status,
                 start_loc,
                 promoted_to_piece=None):
        """
        Constructor to create move using ``Location``

        :type: end_loc: Location
        :type: piece: Piece
        :type: status: int
        """
        self._end_loc = end_loc
        self._status = status
        self._piece = piece
        self._start_loc = start_loc
        self.color = piece.color
        self.promoted_to_piece = promoted_to_piece

    @property
    def end_loc(self):
        return self._end_loc

    @property
    def status(self):
        return self._status

    @property
    def piece(self):
        return self._piece

    def __key(self):
        return self.end_loc, \
               self.piece, \
               self.status, \
               self.start_loc, \
               self.promoted_to_piece

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        """
        Finds if move is same move as this one.
        :type: other: Move
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Cannot compare type {} with Move".format(type(other)))

        for index, item in enumerate(self.__key()):
            if not self._check_equals_or_none(item, other.__key()[index]):
                return False

        return True

    @staticmethod
    def _check_equals_or_none(var1, var2):
        """
        If either is None then return True,
        otherwise compare them and return
        if they are equal.

        :type: var1: object
        :type: var2: object
        :rtype: bool
        """
        if var1 is None or var2 is None:
            return True

        return var1 == var2

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "Move({})".format(self.__dict__)

    def __str__(self):
        """
        Finds string representation in long algebraic notation

        :rtype: str
        """
        move_str = str(self._start_loc) + str(self._end_loc)

        if self.promoted_to_piece is not None:
            move_str += str(self.promoted_to_piece)

        return move_str

    @property
    def start_loc(self):
        """
        Finds start Location of move if specified.
        Otherwise throws an AttributeError

        :rtype: Location
        """
        return self._start_loc

    def would_move_be_promotion(self):
        """
        Finds if move from current location would be a promotion
        """
        return (self._end_loc.rank == 0 and not self.color) or \
            (self._end_loc.rank == 7 and self.color)
