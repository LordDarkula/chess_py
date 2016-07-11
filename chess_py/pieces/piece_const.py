# -*- coding: utf-8 -*-

"""
Constants for piece values in the game

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""


class Piece_values:
    def __init__(self):

        self.PAWN_VALUE = 1

        self.KNIGHT_VALUE = 3

        self.BISHOP_VALUE = 3.5

        self.ROOK_VALUE = 5

        self.QUEEN_VALUE = 9

    @classmethod
    def init_manual(cls, PAWN_VALUE, KNIGHT_VALUE, BISHOP_VALUE, ROOK_VALUE, QUEEN_VALUE):
        """
        Manual init method for external piece values
        :type PAWN_VALUE: float
        :type KNIGHT_VALUE: float
        :type BISHOP_VALUE: float
        :type ROOK_VALUE: float
        :type QUEEN_VALUE: float
        """
        cls.PAWN_VALUE = PAWN_VALUE

        cls.KNIGHT_VALUE = KNIGHT_VALUE

        cls.BISHOP_VALUE = BISHOP_VALUE

        cls.ROOK_VALUE = ROOK_VALUE

        cls.QUEEN_VALUE = QUEEN_VALUE
