# -*- coding: utf-8 -*-

"""
Class stores Pawn on the board

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

from .bishop import Bishop
from .piece import Piece
from .queen import Queen
from .rook import Rook
from .knight import Knight
from ..core import color
from ..core.algebraic import notation_const
from ..core.algebraic.move import Move


class Pawn(Piece):
    def __init__(self, input_color, location):
        """
        Initializes a Pawn that is capable of moving

        :type: input_color: Color
        :type: location: Location
        """
        self.just_moved_two_steps = False
        super(Pawn, self).__init__(input_color, location, "♟", "♙")

    def __str__(self):
        return "P"

    def on_home_row(self, location=None):
        """
        Finds out if the piece is on the home row.

        :return: bool for whether piece is on home row or not
        """
        location = location or self.location
        return (self.color == color.white and location.rank == 1) or \
               (self.color == color.black and location.rank == 6)

    def would_move_be_promotion(self, location=None):
        """
        Finds if move from current get_location would result in promotion

        :type: location: Location
        :rtype: bool
        """
        location = location or self.location
        return (location.rank == 1 and self.color == color.black) or \
                (location.rank == 6 and self.color == color.white)

    def square_in_front(self, location=None):
        """
        Finds square directly in front of Pawn

        :type: location: Location
        :rtype: Location
        """
        location = location or self.location
        return location.shift_up() if self.color == color.white else location.shift_down()

    def two_squares_in_front(self, location):
        """
        Finds square two squares in front of Pawn

        :type: location: Location
        :rtype: get_location
        """
        return self.square_in_front(self.square_in_front(location))

    def create_promotion_moves(self, status, location=None):
        location = location or self.square_in_front()
        def create_each_move(piece):
            return Move(end_loc=location,
                        piece=self,
                        status=status,
                        start_rank=self.location.rank,
                        start_file=self.location.file,
                        promoted_to_piece=piece(self.color, location))

        yield create_each_move(Queen)
        yield create_each_move(Rook)
        yield create_each_move(Bishop)
        yield create_each_move(Knight)

    def forward_moves(self, position):
        """
        Finds possible moves one step and two steps in front
        of Pawn.

        :type: position: Board
        :rtype: list
        """
        if position.is_square_empty(self.square_in_front(self.location)):
            """
            If square in front is empty add the move
            """
            if self.would_move_be_promotion():
                for move in self.create_promotion_moves(notation_const.PROMOTE):
                    yield move
            else:
                yield self.create_move(end_loc=self.square_in_front(self.location),
                                       status=notation_const.MOVEMENT)

            if self.on_home_row() and \
                    position.is_square_empty(self.two_squares_in_front(self.location)):
                """
                If pawn is on home row and two squares in front of the pawn is empty
                add the move
                """
                yield self.create_move(
                    end_loc=self.square_in_front(self.square_in_front(self.location)),
                    status=notation_const.MOVEMENT
                )

    def _one_diagonal_capture_square(self, capture_square, position):
        """
        Adds specified diagonal as a capture move if it is one
        """
        if self.contains_opposite_color_piece(capture_square, position):

            if self.would_move_be_promotion():
                for move in self.create_promotion_moves(status=notation_const.CAPTURE_AND_PROMOTE,
                                                        location=capture_square):
                    yield move

            else:
                yield self.create_move(end_loc=capture_square,
                                       status=notation_const.CAPTURE)

    def capture_moves(self, position):
        """
        Finds out all possible capture moves

        :rtype: list
        """
        try:
            right_diagonal = self.square_in_front(self.location.shift_right())
            for move in self._one_diagonal_capture_square(right_diagonal, position):
                yield move
        except IndexError:
            pass

        try:
            left_diagonal = self.square_in_front(self.location.shift_left())
            for move in self._one_diagonal_capture_square(left_diagonal, position):
                yield move
        except IndexError:
            pass

    def on_en_passant_valid_location(self):
        """
        Finds out if pawn is on enemy center rank.

        :rtype: bool
        """
        return (self.color == color.white and self.location.rank == 4) or \
               (self.color == color.black and self.location.rank == 3)

    def _is_en_passant_valid(self, opponent_pawn_location, position):
        """
        Finds if their opponent's pawn is next to this pawn

        :rtype: bool
        """
        try:
            pawn = position.piece_at_square(opponent_pawn_location)
            return pawn is not None and \
                isinstance(pawn, Pawn) and \
                pawn.color != self.color and \
                position.piece_at_square(opponent_pawn_location).just_moved_two_steps
        except IndexError:
            return False

    def add_one_en_passant_move(self, direction, position):
        """
        Yields en_passant moves in given direction if it is legal.

        :type: direction: function
        :type: position: Board
        :rtype: gen
        """
        try:
            if self._is_en_passant_valid(direction(self.location), position):
                yield self.create_move(
                    end_loc=self.square_in_front(direction(self.location)),
                    status=notation_const.EN_PASSANT
                )
        except IndexError:
            pass

    def en_passant_moves(self, position):
        """
        Finds possible en passant moves.

        :rtype: list
        """

        # if pawn is not on a valid en passant get_location then return None
        if self.on_en_passant_valid_location():
            for move in itertools.chain(self.add_one_en_passant_move(lambda x: x.shift_right(), position),
                                        self.add_one_en_passant_move(lambda x: x.shift_left(), position)):
                yield move

    def possible_moves(self, position):
        """
        Finds out the locations of possible moves given board.Board position.
        :pre get_location is on board and piece at specified get_location on position

        :type: position: Board
        :rtype: list
        """
        for move in itertools.chain(self.forward_moves(position),
                                    self.capture_moves(position),
                                    self.en_passant_moves(position)):
            yield move
