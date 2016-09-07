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


class Move:
    def __init__(self, end_loc, piece, status,
                 start_rank=None,
                 start_file=None,
                 string=None,
                 promoted_to_piece=None):
        """
        Alternate constructor to create move using object algebraic.Location
        :type end_loc: Location
        :type piece: Piece
        :type status: int
        """
        if self.on_board:
            self.end_loc = end_loc

            self.status = status
            self.piece = piece
            self.color = piece.color

            self.start_rank = start_rank
            self.start_file = start_file
            self.promoted_to_piece = promoted_to_piece

            self.string = string
        else:
            self.exit = 1

    def __key(self):
        return self.end_loc, self.piece, self.status, self.start_rank, self.start_file, self.promoted_to_piece

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        """
        Finds if move is same move as this one.
        :type other: Move
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Cannot compare other types with Move")

        if other.status is not None and \
                self.status is not None and \
                other.status != self.status:
            return False

        if other.start_rank is not None and \
                self.start_rank is not None and \
                other.start_rank != self.start_rank:
            return False

        if other.start_file is not None and \
                self.start_file is not None and \
                other.start_file != self.start_file:
            return False

        if other.promoted_to_piece is not None and \
                self.promoted_to_piece is not None and \
                not self.promoted_to_piece.equals(other.promoted_to_piece):
            return False

        return self.end_loc == other.end_loc and \
            self.piece == other.piece and \
            self.status == other.status

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        move_str = str(Location(self.start_rank, self.start_file)) + str(self.end_loc)

        if self.promoted_to_piece is not None:
            move_str += str(self.promoted_to_piece)

        return move_str

    def on_board(self):
        """
        Determines whether move exists.
        :rtype bool
        """
        return self.end_loc.on_board()

    def would_move_be_promotion(self):
        """
        Finds if move from current get_location
        """
        if self.end_loc.rank == 0 and \
                not self.color:
            return True

        if self.end_loc.rank == 7 and \
                self.color:
            return True

        return False

    def out(self):
        print(self.piece.symbol, " Rank: ", self.end_loc.rank, " File:  ", self.end_loc.file, " Status: ", self.status)
