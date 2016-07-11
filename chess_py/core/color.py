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
        :rtype: color.Color
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

    def equals(self, input_color):
        """
        Finds out this color is the same as another color.
        :type input_color: color.Color
        """
        if type(input_color) is type(self):
            return self.color == input_color.color
        else:
            return self.color == input_color
