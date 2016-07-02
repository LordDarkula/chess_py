"""
Parent class for all pieces

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""
from core import color
from core.algebraic.location import Location
from core.algebraic import notation_const


class Piece:
    def __init__(self, input_color, location, white_symbol, black_symbol):
        """
        Initializes a piece that is capable of moving
        :type input_color color.Color
        :type location Location
        :type white_symbol str
        :type black_symbol str
        """
        assert isinstance(input_color, color.Color)
        assert isinstance(location, Location)
        assert isinstance(white_symbol, str)
        assert isinstance(black_symbol, str)

        self.color = input_color
        self.location = location

        if self.color.color == color.white:
            self.symbol = white_symbol
        else:
            self.symbol = black_symbol

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces.py *
        """
        return type(piece) is type(self) and piece.color.equals(self.color.color)

    def set_loc(self, moves):
        """
        Adds start_rank and start_file to moves
        :type moves list
        """
        for i in range(len(moves)):
            moves[i].start_rank = self.location.rank
            moves[i].start_file = self.location.file
