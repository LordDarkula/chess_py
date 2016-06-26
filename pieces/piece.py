"""
Parent class for all pieces

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""
from setup import color
from setup.algebraic_notation.algebraic import Location


class Piece:
    def __init__(self, input_color, location, white_symbol, black_symbol):
        """
        Initializes a piece that is capable of moving
        :type input_color color.Color
        :type location Location
        :type white_symbol str
        :type black_symbol str
        """
        self.location = location
        self.color = input_color

        if self.color.color == color.white:
            self.symbol = white_symbol
        else:
            self.symbol = black_symbol

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces.py *
        """
        return type(piece) is type(self) and piece.color.equals(self.color)