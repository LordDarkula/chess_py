# -*- coding: utf-8 -*-

"""
Class that stores chess moves.
Destination, status and piece making move are required
to initialize Move.

status - integer value describing type of move
with meaning defined in notation_const.py

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""
from chess_py.core.algebraic import notation_const
from chess_py.core.algebraic.location import Location

from chess_py.core import color


class Move:
    string = None
    color = None
    file = None
    rank = None

    status = notation_const.NOT_IMPLEMENTED
    start_rank = None
    start_file = None
    promoted_to_piece = None

    piece = None
    exit = 0

    def __init__(self, location, piece, status, start_rank=None, start_file=None, string=None, promoted_to_piece=None):
        """
        Alternate constructor to create move using object algebraic.Location
        :type location: algebraic.Location
        :type piece: Piece
        :type status: int
        """
        if self.on_board:
            self.rank = location.rank
            self.file = location.file
            self.status = status
            self.piece = piece
            self.color = piece.color

            self.start_rank = start_rank
            self.start_file = start_file
            self.promoted_to_piece = promoted_to_piece

            self.string = string
        else:
            self.exit = 1

    def validate(self):
        """
        Finds if destination is on board.
        :rtype bool
        """
        self.exit = self.end_location().exit

    def equals(self, move):
        """
        Finds if move is same move as this one.
        :type move: algebraic.Move
        """
        return self.rank == move.rank and \
            self.file == move.file and \
            self.piece.equals(move.piece) and \
            self.status == move.status

    def on_board(self):
        """
        Determines whether move exists.
        :rtype bool
        """
        return self.end_location().on_board()

    def end_location(self):
        """
        Finds end location for move.
        :rtype Location
        """
        return Location(self.rank, self.file)

    def would_move_be_promotion(self):
        """
        Finds if move from current location
        """
        if self.rank == 0 and \
                self.color == color.black:
            return True
        elif self.rank == 7 and \
                self.color == color.white:
            return True

        return False

    def out(self):
        print(self.piece.symbol, " Rank: ", self.rank, " File:  ", self.file, " Status: ", self.status)
