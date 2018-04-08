# -*- coding: utf-8 -*-

"""
Easy way to access bool values for black and white without directly
typing True or False.

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""


class Color:

    _color_dict = {
        'white': True,
        'black': False,
    }

    def __init__(self, raw):
        """
        Initializes new color using a boolean
        True is white and False is black

        :type: raw: bool
        """
        self._bool = raw

    @classmethod
    def from_string(cls, string):
        """
        Converts string "white" or "black" into
        corresponding color

        :type: string: str
        :rtype: Color
        """
        return cls(cls._color_dict[string])

    def __repr__(self):
        return "color.{}".format(str(self))

    def __str__(self):
        if self._bool:
            return "white"
        else:
            return "black"

    def __bool__(self):
        return self._bool

    def __int__(self):
        if self._bool:
            return 1
        else:
            return -1

    def __key(self):
        return bool(self)

    def __hash__(self):
        return hash(self.__key())

    def __neg__(self):
        return Color(not self._bool)

    def __eq__(self, other):
        """
        Finds out this color is the same as another color.

        :type: other: Color
        :rtype: bool
        """
        return bool(self) == bool(other)

    def __ne__(self, other):
        return not self.__eq__(other)


white = Color(True)
black = Color(False)
