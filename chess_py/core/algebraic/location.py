# -*- coding: utf-8 -*-

"""
Class stores Locations on the Board.
Locations must be on the board to be initialized properly.
rank - y coordinate from 0 to 7
file - x coordinate from 0 to 7

rank
7 8 ║… … … … … … … …
6 7 ║… … … … … … … …
5 6 ║… … … … … … … …
4 5 ║… … … … … … … …
3 4 ║… … … … … … … …
2 3 ║… … … … … … … …
1 2 ║… … … … … … … …
0 1 ║… … … … … … … …
----╚═══════════════
——---a b c d e f g h
-----0 1 2 3 4 5 6 7
------file

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""


class Location:
    def __init__(self, rank, file):
        """
        Creates a get_location on a chessboard given x and y coordinates.
        :type rank: int
        :type file: int
        """
        self.rank = rank
        self.file = file

    def __key(self):
        return self.rank, self.file

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        """
        Finds is get_location on board is the same as current equation.
        :type other: Location
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Cannot compare other types with Location")

        return int(self.rank) == int(other.rank) and \
            int(self.file) == int(other.file)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        if self.rank is None:
            rank_str = ""
        else:
            rank_str = str(self.rank + 1)

        if self.file is None:
            file_str = ""
        else:
            file_str = chr(self.file + 97)

        return file_str + rank_str

    def on_board(self):
        """
        Returns if the move is on the board or not.
        :rtype bool
        """
        if -1 < self.rank < 8 and \
                -1 < self.file < 8:
            return True

        return False

    def shift_up(self):
        """
        Finds Location shifted up by 1
        :rtype: Location
        """
        return Location(self.rank + 1, self.file)

    def shift_down(self):
        """
        Finds Location shifted down by 1
        :rtype: Location
        """
        return Location(self.rank - 1, self.file)

    def shift_right(self):
        """
        Finds Location shifted right by 1
        :rtype: Location
        """
        return Location(self.rank, self.file + 1)

    def shift_left(self):
        """
        Finds Location shifted left by 1
        :rtype: Location
        """
        return Location(self.rank, self.file - 1)

    def shift_up_right(self):
        """
        Finds Location shifted up right by 1
        :rtype: Location
        """
        return self.shift_up().shift_right()

    def shift_up_left(self):
        """
        Finds Location shifted up left by 1
        :rtype: Location
        """
        return self.shift_up().shift_left()

    def shift_down_right(self):
        """
        Finds Location shifted down right by 1
        :rtype: Location
        """
        return self.shift_down().shift_right()

    def shift_down_left(self):
        """
        Finds Location shifted down left by 1
        :rtype: Location
        """
        return self.shift_down().shift_left()

