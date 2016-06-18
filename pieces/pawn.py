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

from setup import color
from setup.algebraic_notation import algebraic, special_notation_constants


class Pawn:
    def __init__(self, input_color, location):
        """
        Initializes a Pawn that is capable of moving
        :type input_color color.Color
        :type location algebraic.Location
        """
        self.just_moved_two_steps = False
        self.location = location
        self.color = input_color
        if self.color == color.white:
            self.symbol = "♟"
        else:
            self.symbol = "♙"

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces *
        """
        return type(piece) is type(self) and piece.color.equals(self.color)

    def on_home_row(self):
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

    def square_in_front(self, location):
        """
        Finds square directly in front of Pawn
        :rtype algebraic.Location
        """
        if self.color.equals(color.white):
            return location.shift_up()
        else:
            return location.shift_down()
#TODO constructor changed so change everything else that calls this

    def capture_squares(self, position):
        """

        :rtype list
        """
        moves = []
        capture_square = self.location

        def add_capture_square(enemy_color, my_position):
            if not capture_square.exit == 0 and my_position.is_square_empty(capture_square) and my_position.piece_at_square(
                    capture_square).color.equals(enemy_color):
                if self.would_move_be_promotion(self.location):
                    status = special_notation_constants.CAPTURE_AND_PROMOTE
                else:
                    status = special_notation_constants.PROMOTE
                moves.append(algebraic.Move.init_with_location(capture_square, self, status))

        if self.color.equals(color.white):
            capture_square = self.location.shift_up_right()
            add_capture_square(color.black, position)

            capture_square = self.location.shift_up_left()
            add_capture_square(color.black, position)

        else:
            capture_square = self.location.shift_down_right()
            add_capture_square(color.white, position)

            capture_square = self.location.shift_down_left()
            add_capture_square(color.white, position)

        return moves

    def on_en_passant_valid_location(self):
        """
        Finds out if pawn is on enemy center rank.
        """
        print("Running on enemy home row")
        if self.color.equals(color.white) and self.location.rank == 4:

            print("on enemy home row returned true")
            return True
        elif self.color.equals(color.black) and self.location.rank == 3:

            print("on enemy home row returned true")
            return True

        print("on enemy home row returned false")
        return False

    def possible_en_passant_moves(self, position):
        """
        Finds possible en passant moves.
        """
        possible = []



        # if pawn is not on a valid en passant location then return None
        if self.on_en_passant_valid_location():

            # if there is a square on the right and it contains a pawn and the pawn is of opposite color
            if self.location.shift_right().exit == 0 and position.piece_at_square(
                    self.location.shift_right()).equals(Pawn(color.Color(not self.color), self.location)) and position.piece_at_square(
                self.location.shift_right()).just_moved_two_steps:
                possible.append(algebraic.Move.init_with_location(self.location.shift_up_right(), self,
                                                                  special_notation_constants.EN_PASSANT))

            # else if there is a square on the left and it contains a pawn and the pawn is of opposite color
            if self.location.shift_left().exit == 0 and position.piece_at_square(
                    self.location.shift_left()).equals(Pawn(color.Color(not self.color), self.location)) and position.piece_at_square(
                self.location.shift_left()).just_moved_two_steps:
                possible.append(algebraic.Move.init_with_location(self.location.shift_up_left(), self,
                                                                  special_notation_constants.EN_PASSANT))

        return possible

    def would_move_be_promotion(self, location):
        """
        Finds if move from current location
        :type: algebraic.Location
        """

        # If the pawn is on the second rank and black.
        if location.rank == 1 and self.color == color.black:
            return True

        # If the pawn is on the seventh rank and white.
        elif location.rank == 6 and self.color == color.white:
            return True
        return False

    def possible_moves(self, position):
        """
        Finds out the locations of possible moves given board.Board position.
        :pre location is on board and piece at specified location on position
        :param self: pieces.Pawn
        :type position: board.Board
        :rtype list containing algebraic.Location of possible moves
        """
        print('running possible moves')
        moves = []
        #TODO update this bull crap
        # Adds movement to square in front if possible.
        if position.is_square_empty(self.square_in_front(self.location)):
            if self.would_move_be_promotion(self.location):
                status = special_notation_constants.PROMOTE
            else:
                status = special_notation_constants.MOVEMENT
            moves.append(algebraic.Move.init_with_location(self.square_in_front(self.location), self, status))

            # Adds movement to location two squares in front of current location if possible.
            if self.square_in_front(self.location).not_none and self.on_home_row() and position.is_square_empty(
                    self.square_in_front(self.square_in_front(self.location))):
                moves.append(
                    algebraic.Move.init_with_location(self.square_in_front(self.square_in_front(self.location)), self, special_notation_constants.MOVEMENT))

        # Adds all possible capture moves that are returned by possible_capture_moves
        moves.extend(self.capture_squares(position))

        # Adds all possible en passant moves returned by possible_en_passant_moves
        moves.extend(self.possible_en_passant_moves(position))

        return moves