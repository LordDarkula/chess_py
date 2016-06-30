"""
Parent class for all pieces

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""
from setup import color
from pieces.pawn import Pawn
from setup.algebraic.location import Location
from setup.algebraic import notation_const


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
        return type(piece) is type(self) and piece.color.equals(self.color.color)

    def possible_moves(self, moves):
        """
        Adds start_rank and start_file to moves
        :type moves list
        """
        for i in range(len(moves)):
            moves[i].start_rank = self.location.rank
            moves[i].start_file = self.location.file

            if moves[i].status == notation_const.PROMOTE \
                    or moves[i].status == notation_const.CAPTURE_AND_PROMOTE \
                    or moves[i].status == notation_const.EN_PASSANT:
                assert isinstance(moves[i], Pawn)
