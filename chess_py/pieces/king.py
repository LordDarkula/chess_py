# -*- coding: utf-8 -*-

"""
Class stores King on the board

| rank
| 7 8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
| 6 7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
| 5 6 ║… … … … … … … …
| 4 5 ║… … … … … … … …
| 3 4 ║… … … … … … … …
| 2 3 ║… … … … … … … …
| 1 2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
| 0 1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
| ----╚═══════════════
| ——---a b c d e f g h
| -----0 1 2 3 4 5 6 7
| ------file

| Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

import itertools
from copy import copy as cp
from abc import ABCMeta, abstractmethod

from .piece import Piece
from .rook import Rook
from ..core.algebraic import notation_const
from ..core.algebraic.location import Location


class King(Piece):
    def __init__(self, input_color, location):
        """
        Creates a King.

        :type: input_color: Color
        :type: location: Location
        """
        super(King, self).__init__(input_color, location, "♚", "♔")
        self.has_moved = False
        self.cardinal_directions = self.cross_fn + self.diag_fn

    def __str__(self):
        return "K"

    def in_check_as_result(self, pos, move):
        """
        Finds if playing my move would make both kings meet.

        :type: pos: Board
        :type: move: Move
        :rtype: bool
        """
        test = cp(pos)
        test.update(move)
        test_king = test.get_king(move.color)

        return self.loc_adjacent_to_opponent_king(test_king.location, test)

    def loc_adjacent_to_opponent_king(self, location, position):
        """
        Finds if 2 kings are touching given the position of one of the kings.

        :type: location: Location
        :type: position: Board
        :rtype: bool
        """
        for fn in self.cardinal_directions:
            try:
                if isinstance(position.piece_at_square(fn(location)), King) and \
                        position.piece_at_square(fn(location)).color != self.color:
                    return True

            except IndexError:
                pass

        return False

    def add(self, func, position):
        """
        Adds all 8 cardinal directions as moves for the King if legal.

        :type: function: function
        :type: position: Board
        :rtype: gen
        """
        try:
            if self.loc_adjacent_to_opponent_king(func(self.location), position):
                return
        except IndexError:
            return

        if position.is_square_empty(func(self.location)):
            yield self.create_move(func(self.location), notation_const.MOVEMENT)

        elif position.piece_at_square(func(self.location)).color != self.color:
            yield self.create_move(func(self.location), notation_const.CAPTURE)

    def rook_legal_for_castle(self, rook):
        """
        Decides if given rook exists, is of this color, and has not moved so it
        is eligible to castle.

        :type: rook: Rook
        :rtype: bool
        """
        return rook is not None and \
            isinstance(rook, Rook) and \
            rook.color == self.color and \
            not rook.has_moved

    def square_empty_and_not_in_check(self, position, direction, times):
        """
        Checks if set of squares in between ``King`` and ``Rook`` are empty and safe
        for the king to castle.

        :type: position: Position
        :type: direction: function
        :type: times: int
        :rtype: bool
        """
        location = direction(self.location)

        for _ in range(times):

            if not position.is_square_empty(location) or \
                    self.in_check(position, location=location):
                return False

            location = direction(location)

        return True

    class Castle:
        __metaclass__ = ABCMeta

        @abstractmethod
        def rook_file(self):
            pass

        @abstractmethod
        def direction(self):
            pass

        @abstractmethod
        def status(self):
            pass

        @abstractmethod
        def num_squares_moved_by_king(self):
            pass

    class King_side_castle(Castle):
        def __init__(self):
            pass

        @property
        def rook_file(self):
            return 7

        @property
        def direction(self):
            return lambda x: x.shift_right()

        @property
        def status(self):
            return notation_const.KING_SIDE_CASTLE

        @property
        def num_squares_moved_by_king(self):
            return 2

    class Queen_side_castle(Castle):
        def __init__(self):
            pass

        @property
        def rook_file(self):
            return 0

        @property
        def direction(self):
            return lambda x: x.shift_left()

        @property
        def status(self):
            return notation_const.QUEEN_SIDE_CASTLE

        @property
        def num_squares_moved_by_king(self):
            return 3

    def add_one_castle(self, castle, position):
        """
        Adds a castle move given the type of castle.
        
        :type: castle: Castle 
        """
        if self.rook_legal_for_castle(position.piece_at_square(Location(self.location.rank, castle.rook_file))) and \
                self.square_empty_and_not_in_check(position, castle.direction, castle.num_squares_moved_by_king):

            king_after_castle_loc = self.location
            for i in range(castle.num_squares_moved_by_king):
                king_after_castle_loc = castle.direction(king_after_castle_loc)

            yield self.create_move(king_after_castle_loc, castle.status)

    def add_castle(self, position):
        """
        Adds kingside and queenside castling moves if legal

        :type: position: Board
        """
        if self.has_moved or self.in_check(position):
            return

        # Combines 2 generators and iterates through them
        for move in itertools.chain(self.add_one_castle(self.King_side_castle(), position),
                                   self.add_one_castle(self.Queen_side_castle(), position)):
            yield move

    def possible_moves(self, position):
        """
        Generates list of possible moves

        :type: position: Board
        :rtype: list
        """
        # Chain used to combine multiple generators
        for move in itertools.chain(*[self.add(fn, position) for fn in self.cardinal_directions]):
            yield move

        for move in self.add_castle(position):
            yield move

    def in_check(self, position, location=None):
        """
        Finds if the king is in check or if both kings are touching.

        :type: position: Board
        :return: bool
        """
        location = location or self.location
        for piece in position:

            if piece is not None and piece.color != self.color:
                if not isinstance(piece, King):
                    for move in piece.possible_moves(position):

                        if move.end_loc == location:
                            return True
                else:
                    if self.loc_adjacent_to_opponent_king(piece.location, position):
                        return True

        return False
