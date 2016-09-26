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

        :type raw: str
        :rtype: Color
        """
        self.color = raw.upper() == "WHITE"
        self.string = raw

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
        return self.string

    def __key(self):
        return self.color, self.string

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        """
        Finds out this color is the same as another color.

        :type other: Color
        :rtype: bool
        """
        if type(other) is type(self):
            return self.color == other.color

        return self.color == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def opponent(self):
        """
        Finds other color

        :rtype: Color
        """
        return self._boolean(not self.color)

white = Color.pwhite()
black = Color.pblack()


def raw(string):
    """
    Converts string "white" or "black" into
    corresponding color

    :type string: str
    :rtype: Color
    """
    return Color(string)
