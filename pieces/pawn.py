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

"""

from setup import color
from setup.algebraic_notation import algebraic, special_notation_constants


class Pawn:
    def __init__(self, input_color):
        """
        Initializes a Pawn that is capable of moving
        :type input_color color.Color
        """
        self.just_moved_two_steps = False
        self.color = input_color.color

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces *
        """
        return type(piece) is type(self) and piece.color == self.color

    def square_in_front(self, location):
        """
        Finds square directly in front of Pawn
        :type location: algebraic.Location
        :rtype algebraic.Location
        """
        if self.color.equals(color.white):
            return location.shift_up()

        else:
            return location.shift_down()

    def on_home_row(self, location):
        """
        Finds out if the piece is on the home row.
        :type location: location: algebraic.Location
        :return bool for whether piece is on home row or not
        """
        print("Running on home row")

        if self.color.equals(color.white) and location.rank == 1:

            print("on home row returned true")
            return True
        elif self.color.equals(color.black) and location.rank == 6:

            print("on enemy home row returned true")
            return True
        else:

            print("on home row returned false")
            return False

    def possible_capture_moves(self, location, position):
        """
        Returns the squares to the right and left of the square in front.
        Those squares are used for potential captures.
        :type location: algebraic.Location
        :type position: board.Board
        :rtype list
        """
        possible = []
        # Adds capture on right diagonal capture if possible
        if location.shift_up_right().not_none and not position.is_square_empty(
                location.shift_right()) and position.piece_at_square(
                location.shift_right()).color != self.color:
            possible.append(algebraic.Move.init_with_location(location.shift_up_right(), self,
                                                              special_notation_constants.CAPTURE))

        # Adds capture on left diagonal capture if possible
        if location.shift_up_left().not_none and not position.is_square_empty(
                location.shift_up_left()) and position.piece_at_square(
                location.shift_up_left()).color != self.color:
            possible.append(algebraic.Move.init_with_location(location.shift_up_left(), self,
                                                              special_notation_constants.CAPTURE))

        return possible

    def on_en_passant_valid_location(self, location):
        """
        Finds out if pawn is on enemy center rank.
        :type location: algebraic.Location
        """
        print("Running on enemy home row")
        if self.color.equals(color.white) and location.rank == 4:

            print("on enemy home row returned true")
            return True
        elif self.color.equals(color.black) and location.rank == 3:

            print("on enemy home row returned true")
            return True

        print("on enemy home row returned false")
        return False

    def possible_en_passant_moves(self, location, position):
        """
        Finds possible en passant moves.
        :type location: algebraic.location
        :type position: board.Board
        """
        possible = []

        # if pawn is not on a valid en passant location then return None
        if self.on_en_passant_valid_location(location):

            # if there is a square on the right and it contains a pawn and the pawn is of opposite color
            if location.shift_right().not_none and position.piece_at_square(
                    location.shift_right()).equals(Pawn(color.Color(not self.color))) and position.piece_at_square(
                location.shift_right()).just_moved_two_steps:
                possible.append(algebraic.Move.init_with_location(location.shift_up_right(), self,
                                                                  special_notation_constants.EN_PASSANT))

            # else if there is a square on the left and it contains a pawn and the pawn is of opposite color
            if location.shift_left().not_none and position.piece_at_square(
                    location.shift_left()).equals(Pawn(color.Color(not self.color))) and position.piece_at_square(
                location.shift_left()).just_moved_two_steps:
                possible.append(algebraic.Move.init_with_location(location.shift_up_left(), self,
                                                                  special_notation_constants.EN_PASSANT))

        return possible

    #TODO add promotion
    
    def possible_moves(self, location, position):
        """
        Finds out the locations of possible moves given board.Board position.
        :pre location is on board and piece at specified location on position
        :param self: pieces.Pawn
        :type location: algebraic.location
        :type position: board.Board
        :rtype list containing algebraic.Location of possible moves
        """
        print('running possible moves')
        moves = []

        # Adds movement to square in front if possible.
        if self.square_in_front(location).not_none and position.is_square_empty(self.square_in_front(location)):
            moves.append(algebraic.Move.init_with_location(self.square_in_front(location), self,
                                                           special_notation_constants.MOVEMENT))

            # Adds movement to location two squares in front of current location if possible.
            if self.square_in_front(location).not_none and self.on_home_row(location) and position.is_square_empty(
                    self.square_in_front(self.square_in_front(location))):
                moves.append(
                    algebraic.Move.init_with_location(self.square_in_front(self.square_in_front(location)), self,
                                                      special_notation_constants.MOVEMENT))

        moves.extend(self.possible_capture_moves(location, position))
        moves.extend(self.possible_en_passant_moves(location, position))

        return moves

