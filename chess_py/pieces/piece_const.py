# -*- coding: utf-8 -*-

"""
Constants for piece values in the game

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from .bishop import Bishop
from .pawn import Pawn
from .queen import Queen
from .rook import Rook
from .knight import Knight


class PieceValues:
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

        :type: PAWN_VALUE: double
        :type: KNIGHT_VALUE: double
        :type: BISHOP_VALUE: double
        :type: ROOK_VALUE: double
        :type: QUEEN_VALUE: double
        """
        piece_values = cls()
        piece_values.PAWN_VALUE = PAWN_VALUE
        piece_values.KNIGHT_VALUE = KNIGHT_VALUE
        piece_values.BISHOP_VALUE = BISHOP_VALUE
        piece_values.ROOK_VALUE = ROOK_VALUE
        piece_values.QUEEN_VALUE = QUEEN_VALUE
        return piece_values

    def val(self, piece, ref_color):
        """
        Finds value of ``Piece``

        :type: piece: Piece
        :type: ref_color: Color
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
        elif isinstance(piece, Queen):
            return self.QUEEN_VALUE * const
        elif isinstance(piece, Bishop):
            return self.BISHOP_VALUE * const
        elif isinstance(piece, Rook):
            return self.ROOK_VALUE * const
        return 0
