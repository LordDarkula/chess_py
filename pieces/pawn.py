import algebraic
import equality
import color

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

class Piece:
:type color: keyword "white" or "black"
"""


class Pawn:
    def __init__(self, color):

        """
        Initializes a Pawn that is capable of moving
        :type color.Color
        """
        self.just_moved_two_steps = False
        self.color = color

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces *
        """
        return type(piece) is type(self) and piece.color == self.color

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

            return True
        else:

            print("on home row returns false")
            return False

    def square_in_front(self, location):

        """
        Finds square directly in front of Pawn
        :type location: algebraic.Location
        """

        if self.color.equals(color.white):
            return location.shift_up()

        else:
            return location.shift_down()

    def can_en_passant(self, location, position):

        """
        Finds out if pawn can en passant.
        :type location: algebraic.location
        :type position: board.Board
        """

        """
        if piece is white
        """
        if self.color.equals(color.white) and location.rank == 4:

            """
            if there is a square on the right and it contains a pawn and the pawn is black
            """
            if equality.location_not_none(location.shift_right()) and position.piece_at_square(
                    location.shift_right()).equals(Pawn(color.black)) and position.piece_at_square(
                location.shift_right()).just_moved_two_steps:
                return True

            """
            else if there is a square on the left and it contains a pawn and the pawn is black
            """
            if equality.location_not_none(location.shift_left()) and position.piece_at_square(
                    location.shift_left()).equals(Pawn(color.black)) and position.piece_at_square(
                location.shift_left()).just_moved_two_steps:
                return True

            return False


        elif self.color.equals(color.black) and location.rank == 3:
            """
            if there is a square on the right and it contains a pawn and the pawn is white
            """
            if equality.location_not_none(location.shift_right()) and position.piece_at_square(
                    location.shift_right()).equals(Pawn(color.white)) and position.piece_at_square(
                    location.shift_right).just_moved_two_steps:
                return True

            """
            else if there is a square on the left and it contains a pawn and the pawn is white
            """
            if equality.location_not_none(location.shift_left()) and position.piece_at_square(
                    location.shift_left().equals(Pawn(color.white))) and position.piece_at_square(
                    location.shift_left).just_moved_two_steps:
                return True

            return False

        return False

    def possible_moves(self, location, position):

        """
        Finds out the locations of possible moves given board.Board position.
        :pre piece is actually on specified location on position
        :param self: pieces.Pawn
        :type location: algebraic.location
        :type position: board.Board
        :return list containing algebraic.Location of possible moves
        """
        print('running possible moves')
        moves = []

        """
        if this pawn is on home row and board's square in front of front of this pawn is empty
        precondition: location not at edge of board
        """
        if self.on_home_row(location) and position.is_square_empty(
                self.square_in_front(self.square_in_front(location))):
            moves.append(self.square_in_front(self.square_in_front(location)))

        if self.can_en_passant(location, position):
            # TODO figure out how to add en passant
            print("")

        if self.square_in_front(location) is not None and position.is_square_empty(self.square_in_front(location)):
            moves.append(self.square_in_front(location))
        """
        if there is a square in front this pawn and the square is empty
        """
        # TODO add capture functionality
        return moves
