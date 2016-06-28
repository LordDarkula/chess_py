#TODO verify code and finalize class documentation

"""

rank
7 8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
6 7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
5 6 ║… … … … … … … …
4 5 ║… … … … … … … …
3 4 ║… … … … … … … …
2 3 ║… … … … … … … …
1 2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
0 1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
----╚═══════════════
——---a b c d e f g h
-----0 1 2 3 4 5 6 7
------file

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from setup.algebraic_notation.location import Location
from setup.algebraic_notation.move import Move
from setup.algebraic_notation import notation_const
from pieces import piece
from setup import color


class Pawn(piece.Piece):
    def __init__(self, input_color, location):
        """
        Initializes a Pawn that is capable of moving
        :type input_color color.Color
        :type location Location
        """
        self.just_moved_two_steps = False
        super(Pawn, self).__init__(input_color, location, "♟", "♙")

    def square_in_front(self, location):
        """
        Finds square directly in front of Pawn
        :type location Location
        :rtype Location
        """
        if self.color.equals(color.white):
            return location.shift_up()
        else:
            return location.shift_down()

    def two_squares_in_front(self, location):
        """
        Finds square two squares in front of Pawn
        :param location: Location
        :rtype location
        """
        return self.square_in_front(self.square_in_front(location))

    def would_move_be_promotion(self, location):
        """
        Finds if move from current location
        :type: Location
        :rtype: bool
        """

        # If the pawn is on the second rank and black.
        if location.rank == 1 and self.color.color == color.black:
            return True

        # If the pawn is on the seventh rank and white.
        elif location.rank == 6 and self.color.color == color.white:
            return True
        return False

    def forward_moves(self, position):
        """
        Finds all possible forward moves
        :type: position: board.Board
        :rtype: list
        """
        possible = []

        def on_home_row():
            """
            Finds out if the piece is on the home row.
            :return bool for whether piece is on home row or not
            """
            if self.color.equals(color.white) and self.location.rank == 1:
                return True
            elif self.color.equals(color.black) and self.location.rank == 6:
                return True
            else:
                return False

        if on_home_row() and position.is_square_empty(self.square_in_front(self.location)):
            """
            If the pawn is on home row and square in front is empty add the move
            """
            possible.append(Move(self.square_in_front(self.location), self, notation_const.MOVEMENT))

            if position.is_square_empty(self.two_squares_in_front(self.location)):
                """
                If two squares in front of the pawn is empty add the move
                """
                possible.append(Move(self.square_in_front(self.square_in_front(self.location)), self, notation_const.MOVEMENT))

        elif position.is_square_empty(self.square_in_front(self.location)):
            """
            Else if square in front is empty add the move
            """
            if self.would_move_be_promotion(self.location):
                status = notation_const.PROMOTE
            else:
                status = notation_const.MOVEMENT
            move = Move(self.square_in_front(self.location), self, status)

            possible.append(move)

        return possible

    def capture_moves(self, position):
        """
        Finds out all possible capture moves
        :rtype list
        """
        moves = []
        capture_square = self.location

        def add_capture_square():
            """
            Adds capture moves
            """
            if not position.is_square_empty(capture_square) and position.piece_at_square(capture_square).color.equals(not self.color.color):
                """
                If the capture square is nit empty and it contains a piece of opposing color add the move
                """
                if self.would_move_be_promotion(self.location):
                    """
                    If the move results in promotion take not if that
                    """
                    status = notation_const.CAPTURE_AND_PROMOTE
                else:

                    status = notation_const.PROMOTE

                moves.append(Move(capture_square, self, status))

        capture_square = self.square_in_front(self.location.shift_right())
        add_capture_square()

        capture_square = self.square_in_front(self.location.shift_left)
        add_capture_square()

        return moves

    def en_passant_moves(self, position):
        """
        Finds possible en passant moves.
        """
        possible = []

        def on_en_passant_valid_location():
            """
            Finds out if pawn is on enemy center rank.
            """
            if self.color.equals(color.white) and self.location.rank == 4:
                return True

            elif self.color.equals(color.black) and self.location.rank == 3:
                return True

            return False

        def opposite_color_pawn_on_square(my_location):
            """

            :rtype: bool
            """
            return my_location.exit == 0 and position.piece_at_square(my_location).equals(Pawn(color.Color(not self.color), my_location)) and position.piece_at_square(
                my_location).just_moved_two_steps

        # if pawn is not on a valid en passant location then return None
        if on_en_passant_valid_location():

            # if there is a square on the right and it contains a pawn and the pawn is of opposite color
            if opposite_color_pawn_on_square(self.location.shift_right):
                possible.append(Move(self.square_in_front(self.location.shift_right()), self,notation_const.EN_PASSANT))

            # else if there is a square on the left and it contains a pawn and the pawn is of opposite color
            if opposite_color_pawn_on_square(self.location.shift_left):
                possible.append(Move(self.square_in_front(self.location.shift_left()), self, notation_const.EN_PASSANT))

        return possible

    def possible_moves(self, position):
        """
        Finds out the locations of possible moves given board.Board position.
        :pre location is on board and piece at specified location on position
        :type position: board.Board
        :rtype list
        """
        moves = []

        # Adds all possible forward moves that are returned by forward_movs
        moves.extend(self.forward_moves(position))

        # Adds all possible capture moves that are returned by possible_capture_moves
        moves.extend(self.capture_moves(position))

        # Adds all possible en passant moves returned by en_passant_moves
        moves.extend(self.en_passant_moves(position))

        return moves