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
        :type: input_color color.Color
        :type: location Location
        """
        self.just_moved_two_steps = False
        super(Pawn, self).__init__(input_color, location, "♟", "♙")

    def __str__(self):
        return "P"

    def on_home_row(self):
        """
        Finds out if the piece is on the home row.

        :return bool for whether piece is on home row or not
        """
        if self.color == color.white and self.location.rank == 1:
            return True
        elif self.color == color.black and self.location.rank == 6:
            return True
        else:
            return False

    def square_in_front(self, location):
        """
        Finds square directly in front of Pawn
        :type: location Location
        :rtype Location
        """
        if self.color == color.white:
            return location.shift_up()
        else:
            return location.shift_down()

    def two_squares_in_front(self, location):
        """
        Finds square two squares in front of Pawn
        :type: location: Location
        :rtype get_location
        """
        return self.square_in_front(self.square_in_front(location))

    def would_move_be_promotion(self, location):
        """
        Finds if move from current get_location would result in promotion
        :type:: Location
        :rtype: bool
        """

        # If the pawn is on the second rank and black.
        if location.rank == 1 and \
                self.color == color.black:
            return True

        # If the pawn is on the seventh rank and white.
        elif location.rank == 6 and \
                self.color == color.white:
            return True
        return False

    def create_promotion_moves(self, location, status):
        moves = []

        def create_each_move(piece):
            move = Move(end_loc=location,
                        piece=self,
                        status=status,
                        start_rank=self.location.rank,
                        start_file=self.location.file,
                        promoted_to_piece=piece(self.color, location))

            moves.append(move)

        create_each_move(Queen)
        create_each_move(Rook)
        create_each_move(Bishop)
        create_each_move(Knight)

        return moves

    def forward_moves(self, position):
        """
        Finds possible moves one step and two steps in front
        of Pawn.

        :type:: position: Board
        :rtype: list
        """
        possible = []

        if position.is_square_empty(self.square_in_front(self.location)):
            """
            If square in front is empty add the move
            """
            if self.would_move_be_promotion(self.location):
                possible.extend(self.create_promotion_moves(self.square_in_front(self.location),
                                                            notation_const.PROMOTE))
            else:
                move = Move(end_loc=self.square_in_front(self.location),
                            piece=self,
                            status=notation_const.MOVEMENT,
                            start_rank=self.location.rank,
                            start_file=self.location.file)

                possible.append(move)

            if self.on_home_row() and position.is_square_empty(self.two_squares_in_front(self.location)):
                """
                If two squares in front of the pawn is empty add the move
                """
                possible.append(Move(end_loc=self.square_in_front(self.square_in_front(self.location)),
                                     piece=self,
                                     status=notation_const.MOVEMENT,
                                     start_rank=self.location.rank,
                                     start_file=self.location.file))

        return possible

    def capture_moves(self, position):
        """
        Finds out all possible capture moves

        :rtype: list
        """
        moves = []
        capture_square = self.location

        def add_capture_square():
            """
            Adds capture moves
            """
            if self.contains_opposite_color_piece(capture_square, position):
                """
                If the capture square is not empty and it contains a piece of opposing color add the move
                """
                if self.would_move_be_promotion(self.location):
                    moves.extend(self.create_promotion_moves(capture_square, notation_const.CAPTURE_AND_PROMOTE))

                else:
                    move = Move(end_loc=capture_square,
                                piece=self,
                                status=notation_const.CAPTURE,
                                start_rank=self.location.rank,
                                start_file=self.location.file)

                    moves.append(move)

        capture_square = self.square_in_front(self.location.shift_right())
        add_capture_square()

        capture_square = self.square_in_front(self.location.shift_left())
        add_capture_square()

        return moves

    def en_passant_moves(self, position):
        """
        Finds possible en passant moves.

        :rtype: list
        """
        possible = []

        def on_en_passant_valid_location():
            """
            Finds out if pawn is on enemy center rank.

            :rtype: bool
            """
            if self.color == color.white and \
                    self.location.rank == 4:
                return True

            elif self.color == color.black and \
                    self.location.rank == 3:
                return True

            return False

        def opposite_color_pawn_on_square(my_location):
            """
            Finds if their is opponent's pawn is next to this pawn

            :rtype: bool
            """
            return my_location.on_board() and \
                not position.is_square_empty(my_location) and \
                position.piece_at_square(my_location) == Pawn(self.color.opponent(), my_location) and \
                position.piece_at_square(my_location).just_moved_two_steps

        # if pawn is not on a valid en passant get_location then return None
        if on_en_passant_valid_location():

            # if there is a square on the right and it contains a pawn and the pawn is of opposite color
            if opposite_color_pawn_on_square(self.location.shift_right()):
                possible.append(Move(end_loc=self.square_in_front(self.location.shift_right()),
                                     piece=self,
                                     status=notation_const.EN_PASSANT,
                                     start_rank=self.location.rank,
                                     start_file=self.location.file))

            # else if there is a square on the left and it contains a pawn and the pawn is of opposite color
            if opposite_color_pawn_on_square(self.location.shift_left()):
                possible.append(Move(end_loc=self.square_in_front(self.location.shift_left()),
                                     piece=self,
                                     status=notation_const.EN_PASSANT,
                                     start_rank=self.location.rank,
                                     start_file=self.location.file))

        return possible

    def possible_moves(self, position):
        """
        Finds out the locations of possible moves given board.Board position.
        :pre get_location is on board and piece at specified get_location on position
        :type: position: board.Board
        :rtype list
        """
        moves = []

        if self.forward_moves(position) is not None:
            # Adds all possible forward moves that are returned by forward_movs
            moves.extend(self.forward_moves(position))

        if self.capture_moves(position) is not None:
            # Adds all possible capture moves that are returned by possible_capture_moves
            moves.extend(self.capture_moves(position))

        if self.en_passant_moves(position) is not None:
            # Adds all possible en passant moves returned by en_passant_moves
            moves.extend(self.en_passant_moves(position))

        return moves
