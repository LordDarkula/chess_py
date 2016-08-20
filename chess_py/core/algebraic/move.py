# -*- coding: utf-8 -*-

"""
Class that stores chess moves.
Destination, status and piece making move are required
to initialize Move.

status - integer value describing type of move
with meaning defined in notation_const.py

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from chess_py.core.algebraic.location import Location

from chess_py.core import color


class Move:
    def __init__(self, start_loc, piece, status, start_rank=None, start_file=None, string=None, promoted_to_piece=None):
        """
        Alternate constructor to create move using object algebraic.Location
        :type location: Location
        :type piece: Piece
        :type status: int
        """
        if self.on_board:
            self.start_loc = start_loc

            self.status = status
            self.piece = piece
            self.color = piece.color

            self.start_rank = start_rank
            self.start_file = start_file
            self.promoted_to_piece = promoted_to_piece

            self.string = string
        else:
            self.exit = 1

    def equals(self, move):
        """
        Finds if move is same move as this one.
        :type move: algebraic.Move
        """
        return self.start_loc.equals(move.start_loc) and \
            self.piece.equals(move.piece) and \
            self.status == move.status

    def on_board(self):
        """
        Determines whether move exists.
        :rtype bool
        """
        return self.start_loc.on_board()

    def would_move_be_promotion(self):
        """
        Finds if move from current get_location
        """
        if self.start_loc.rank == 0 and \
                self.color == color.black:
            return True

        if self.start_loc.rank == 7 and \
                self.color == color.white:
            return True

        return False

    def out(self):
        print(self.piece.symbol, " Rank: ", self.start_loc.rank, " File:  ", self.start_loc.file, " Status: ", self.status)
