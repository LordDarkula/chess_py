# -*- coding: utf-8 -*-

"""
Class stores Locations on the Board in form ``Location(rank, file)``.

| rank - y coordinate from 0 to 7
| file - x coordinate from 0 to 7

Can be initialized with coordinates not
on the chess board, however, such locations
will not work properly with other classes
such as ``Board``.

Location is immutable.

Examples (shown on board below):

| a = Location(0, 0)
| b = Location(7, 7)
| c = Location(3, 4)

| rank
| 7 8 ║… … … … … … … b
| 6 7 ║… … … … … … … …
| 5 6 ║… … … … … … … …
| 4 5 ║… … … … … … … …
| 3 4 ║… … … … c … … …
| 2 3 ║… … … … … … … …
| 1 2 ║… … … … … … … …
| 0 1 ║a … … … … … … …
| ----╚═══════════════
| ——---a b c d e f g h
| -----0 1 2 3 4 5 6 7
| ------file

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""


class Direction:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Location:
    def __init__(self, rank, file):
        """
        Creates a location on a chessboard given x and y coordinates.

        :type: rank: int
        :type: file: int
        """
        if rank < 0 or rank > 7 or file < 0 or file > 7:
            raise IndexError("Location must be on the board")

        self._rank = rank
        self._file = file

    @classmethod
    def from_string(cls, alg_str):
        """
        Creates a location from a two character string consisting of 
        the file then rank written in algebraic notation.
        
        Examples: e4, b5, a7

        :type: alg_str: str
        :rtype: Location
        """
        return cls(int(alg_str[1]) - 1, ord(alg_str[0]) - 97)

    @property
    def rank(self):
        return self._rank

    @property
    def file(self):
        return self._file

    def __key(self):
        return self.rank, self.file

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        """
        Tests to see if both locations
        are the same ie rank and file is 
        the same.

        :type: other: Location
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Cannot compare other types with Location")

        return int(self.rank) == int(other.rank) and \
            int(self.file) == int(other.file)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        """
        Finds string representation of Location in algebraic form ie "e4"

        :rtype: str
        """
        if self._rank is None:
            rank_str = ""
        else:
            rank_str = str(self._rank + 1)

        if self._file is None:
            file_str = ""
        else:
            file_str = chr(self._file + 97)

        return file_str + rank_str

    def on_board(self):
        """
        Returns if the move is on the board or not.
        If the rank and file are both in between
        0 and 7, this method will return True.

        :rtype: bool
        """
        if -1 < self._rank < 8 and \
                -1 < self._file < 8:
            return True

        return False

    def shift(self, direction):
        """
        Shifts in direction provided by ``Direction`` enum.

        :type: direction: Direction
        :rtype: Location
        """
        try:
            if direction == Direction.UP:
                return self.shift_up()
            elif direction == Direction.DOWN:
                return self.shift_down()
            elif direction == Direction.RIGHT:
                return self.shift_right()
            elif direction == Direction.LEFT:
                return self.shift_left()
            else:
                raise IndexError("Invalid direction {}".format(direction))
        except IndexError as e:
            raise IndexError(e)

    def shift_up(self):
        """
        Finds Location shifted up by 1

        :rtype: Location
        """
        try:
            return Location(self._rank + 1, self._file)
        except IndexError as e:
            raise IndexError(e)

    def shift_down(self):
        """
        Finds Location shifted down by 1

        :rtype: Location
        """
        try:
            return Location(self._rank - 1, self._file)
        except IndexError as e:
            raise IndexError(e)

    def shift_right(self):
        """
        Finds Location shifted right by 1

        :rtype: Location
        """
        try:
            return Location(self._rank, self._file + 1)
        except IndexError as e:
            raise IndexError(e)

    def shift_left(self):
        """
        Finds Location shifted left by 1

        :rtype: Location
        """
        try:
            return Location(self._rank, self._file - 1)
        except IndexError as e:
            raise IndexError(e)

    def shift_up_right(self):
        """
        Finds Location shifted up right by 1

        :rtype: Location
        """
        try:
            return self.shift_up().shift_right()
        except IndexError as e:
            raise IndexError(e)

    def shift_up_left(self):
        """
        Finds Location shifted up left by 1

        :rtype: Location
        """
        try:
            return self.shift_up().shift_left()
        except IndexError as e:
            raise IndexError(e)

    def shift_down_right(self):
        """
        Finds Location shifted down right by 1

        :rtype: Location
        """
        try:
            return self.shift_down().shift_right()
        except IndexError as e:
            raise IndexError(e)

    def shift_down_left(self):
        """
        Finds Location shifted down left by 1

        :rtype: Location
        """
        try:
            return self.shift_down().shift_left()
        except IndexError as e:
            raise IndexError(e)
