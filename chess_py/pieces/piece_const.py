# -*- coding: utf-8 -*-

"""
Constants for piece values in the game

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from chess_py.pieces.bishop import Bishop
from chess_py.pieces.pawn import Pawn
from chess_py.pieces.queen import Queen
from chess_py.pieces.rook import Rook
from chess_py.pieces.knight import Knight


class Piece_values:
    def __init__(self):

        self.PAWN_VALUE = 1

        self.KNIGHT_VALUE = 3

        self.BISHOP_VALUE = 3

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

    def val(self, piece, ref_color):
        """
        Finds value of piece
        :type piece: Piece
        :type ref_color: Color
        :rtype: int
        """
        if piece is None:
            return 0

        if ref_color == piece.color:
            const = 1
        else:
            const = -1

        if isinstance(piece, Pawn):
            return self.PAWN_VALUE * const
        elif isinstance(piece, Knight):
            return self.KNIGHT_VALUE * const
        elif isinstance(piece, Bishop):
            return self.BISHOP_VALUE * const
        elif isinstance(piece, Rook):
            return self.ROOK_VALUE * const
        elif isinstance(piece, Queen):
            return self.QUEEN_VALUE * const
        return 0

