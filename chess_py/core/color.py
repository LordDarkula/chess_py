# -*- coding: utf-8 -*-

"""
Easy way to access bool values for black and white without directly
typing True or False.

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""


class Color:
    def __init__(self, raw):
        """
        Initializes new color using a string

        :type: raw: str
        :rtype: Color
        """
        self._color = raw.upper() == "WHITE"
        self._string = raw

    @classmethod
    def pwhite(cls):
        return cls("white")

    @classmethod
    def pblack(cls):
        return cls("black")

    @classmethod
    def _boolean(cls, boolean):
        if boolean:
            return cls.pwhite()

        return cls.pblack()

    def __str__(self):
        return self._string

    def __key(self):
        return self._color, self._string

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        """
        Finds out this color is the same as another color.

        :type: other: Color
        :rtype: bool
        """
        if isinstance(other, Color):
            return self._string == str(other)

        return self._color == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def opponent(self):
        """
        Finds other color

        :rtype: Color
        """
        return self._boolean(not self._color)

white = Color.pwhite()
black = Color.pblack()


def from_string(string):
    """
    Converts string "white" or "black" into
    corresponding color

    :type: string: str
    :rtype: Color
    """
    return Color(string.lower())
