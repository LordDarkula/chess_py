# -*- coding: utf-8 -*-

"""
Easy way to access bool values for black and white without directly
typing True or False.

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""
white = True
black = False


class Color:
    def __init__(self, color):
        """
        Initializes new color using bool with white = True and black = False

        :type color: bool
        :rtype: Color
        """
        self.color = color
        if color:
            self.string = "white"
        else:
            self.string = "black"

    @classmethod
    def init_white(cls):
        return cls(white)

    @classmethod
    def init_black(cls):
        return cls(black)

    @classmethod
    def init_raw(cls, raw):
        cls.color = raw == "white"
        cls.string = raw

    def __key(self):
        return self.color

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
        return Color(not self.color)
