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
from .king import King


class PieceValues:
    def __init__(self):
        self.PAWN_VALUE = 1
        self.KNIGHT_VALUE = 3
        self.BISHOP_VALUE = 3.5
        self.ROOK_VALUE = 5
        self.QUEEN_VALUE = 9
        self.KING_VALUE = 999

    @classmethod
    def init_manual(cls, pawn_value, knight_value, bishop_value, rook_value, queen_value, king_value):
        """
        Manual init method for external piece values

        :type: PAWN_VALUE: int
        :type: KNIGHT_VALUE: int
        :type: BISHOP_VALUE: int
        :type: ROOK_VALUE: int
        :type: QUEEN_VALUE: int
        """
        piece_values = cls()
        piece_values.PAWN_VALUE = pawn_value
        piece_values.KNIGHT_VALUE = knight_value
        piece_values.BISHOP_VALUE = bishop_value
        piece_values.ROOK_VALUE = rook_value
        piece_values.QUEEN_VALUE = queen_value
        piece_values.KING_VALUE = king_value
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
        elif isinstance(piece, Queen):
            return self.QUEEN_VALUE * const
        elif isinstance(piece, Bishop):
            return self.BISHOP_VALUE * const
        elif isinstance(piece, Rook):
            return self.ROOK_VALUE * const
        elif isinstance(piece, Knight):
            return self.KNIGHT_VALUE * const
        elif isinstance(piece, King):
            return self.KING_VALUE * const
        return 0
