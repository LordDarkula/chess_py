# -*- coding: utf-8 -*-

"""
Constructs board object which stores the get_location of all the pieces.

Default Array

| [[0th row 0th item,  0th row 1st item,  0th row 2nd item],
|  [1st row 0th item,  1st row 1st item,  1st row 2nd item],
|  [2nd row 0th item, 2nd row 1st item,  2nd row 2nd item]]

| Default board
| 8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ Black pieces
| 7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ Black pawns
| 6 ║a6… … … … … …h6
| 5 ║… … … … … … … …
| 4 ║… … … … … … … …
| 3 ║a3… … … … … …h3 Algebraic
| 2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ White pawns
| 1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ White pieces
| -—╚═══════════════
| ——-a b c d e f g h

Pieces on the board are flipped so white home row is at index 0
and black home row is at index 7

| Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from __future__ import print_function

from copy import copy as cp
from math import fabs

from . import color
from .algebraic import notation_const
from .algebraic.location import Location
from ..pieces.piece import Piece
from ..pieces.bishop import Bishop
from ..pieces.king import King
from ..pieces.pawn import Pawn
from ..pieces.queen import Queen
from ..pieces.rook import Rook
from ..pieces.knight import Knight


class Board:
    """
    Standard starting position in a chess game.
    Initialized upon startup and is used when init_default constructor is used

    """
    def __init__(self, position):
        """
        Creates a ``Board`` given an array of ``Piece`` and ``None''
        objects to represent the given position of the board.

        :type: position: list
        """
        self.position = position

    @classmethod
    def init_default(cls):
        """
        Creates a ``Board`` with the standard chess starting position.

        :rtype: Board
        """
        white = color.white
        black = color.black
        return cls([

        # First rank
        [Rook(white, Location(0, 0)), Knight(white, Location(0, 1)), Bishop(white, Location(0, 2)),
         Queen(white, Location(0, 3)), King(white, Location(0, 4)), Bishop(white, Location(0, 5)),
         Knight(white, Location(0, 6)), Rook(white, Location(0, 7))],

        # Second rank
        [Pawn(white, Location(1, file)) for file in range(8)],


        # Third rank
        [None for _ in range(8)],

        # Fourth rank
        [None for _ in range(8)],

        # Fifth rank
        [None for _ in range(8)],

        # Sixth rank
        [None for _ in range(8)],

        # Seventh rank
        [Pawn(black, Location(6, file)) for file in range(8)],

        # Eighth rank
        [Rook(black, Location(7, 0)), Knight(black, Location(7, 1)), Bishop(black, Location(7, 2)),
         Queen(black, Location(7, 3)), King(black, Location(7, 4)), Bishop(black, Location(7, 5)),
         Knight(black, Location(7, 6)), Rook(black, Location(7, 7))]
    ])

    def __key(self):
        return self.position

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):

        if not isinstance(other, self.__class__):
            raise TypeError("Cannot compare other type to Board")

        for i, row in enumerate(self.position):

            for j, piece in enumerate(row):

                if piece != other.position[i][j]:
                    return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        """
        Prints current position in console
        """
        b_str = ""
        # Loops through rows
        for i, row in enumerate(self.position):

            b_str += (str(8 - i) + " ")
            # Loops through squares in each row
            for j, square in enumerate(row):

                piece = self.piece_at_square(Location(7 - i, j))

                # If there is a piece on the square
                if isinstance(piece, Piece):

                    # Prints out symbol of piece
                    b_str += (str(self.position[7 - i][j].symbol) + " ")

                elif piece is None:
                    b_str += "_ "

                else:
                    b_str += str(piece) + " "

            b_str += "\n"

        b_str += "  a b c d e f g h"

        return b_str

    def __iter__(self):
        for row in self.position:
            for square in row:
                yield square

    def __copy__(self):
        """
        Copies the board faster than deepcopy

        :rtype: Board
        """
        self.board = Board([[cp(piece) for piece in self.position[index]] for index, row in enumerate(self.position)])
        return self.board

    def piece_at_square(self, location):
        """
        Finds the chess piece at a square of the position.

        :type:: location Location
        :rtype: Piece
        """
        return self.position[location.rank][location.file]

    def is_square_empty(self, location):
        """
        Finds whether a chess piece occupies a square of the position.

        :type: location: Location
        :rtype: bool
        """
        return self.position[location.rank][location.file] is None

    def material_advantage(self, input_color, val_scheme):
        """
        Finds the advantage a particular side possesses given a value scheme.

        :type: input_color: Color
        :type: val_scheme: Piece_values
        :rtype: double
        """
        if self.get_king(input_color).in_check(self) and len(self.all_possible_moves(input_color)) == 0:
            return -100

        if self.get_king(input_color.opponent()).in_check(self) and \
                        len(self.all_possible_moves(input_color.opponent())) == 0:
            return 100

        advantage = 0.0
        for row in self.position:
            for piece in row:
                advantage += val_scheme.val(piece=piece, ref_color=input_color)

        return advantage

    def advantage_as_result(self, move, val_scheme):
        """
        Calculates advantage after move is played

        :type: move: Move
        :type: val_scheme: Piece_values
        :rtype: double
        """
        test_board = cp(self)
        test_board.update(move)
        return test_board.material_advantage(move.color, val_scheme)

    def all_possible_moves(self, input_color):
        """
        Returns list of all possible moves

        :type: input_color: Color
        :rtype: list
        """
        moves = []

        # Loops through columns
        for row in self.position:

            # Loops through rows
            for piece in row:

                    # Tests if square on the board is not empty
                    if piece is not None and piece.color == input_color:

                        # Adds all of piece's possible moves to moves list.
                        if self.get_king(input_color).in_check(self):
                            print("King in check")

                            """
                            Loops through all of the King's responses to
                            see if they get it out of check
                            """
                            for move in piece.possible_moves(self):
                                test = cp(self)
                                test.update(move)

                                # If the King's response gets it out of check, it is legal
                                if not test.get_king(input_color).in_check(test):
                                    moves.append(move)
                        else:
                            moves.extend(piece.possible_moves(self))

        return moves

    def find_piece(self, piece):
        """
        Finds Location of the first piece that matches piece.
        If none is found, Exception is raised.

        :type: piece: Piece
        :rtype: Location
        """
        for i in range(len(self.position)):

            for j in range(len(self.position)):
                loc = Location(i, j)
                if not self.is_square_empty(loc) and \
                        self.piece_at_square(loc) == piece:
                    return loc

        raise Exception("Piece not found: " + str(piece))

    def get_piece(self, piece_type, input_color):
        for i in range(len(self.position)):

            for j in range(len(self.position)):
                loc = Location(i, j)
                piece = self.piece_at_square(loc)

                if not self.is_square_empty(loc) and \
                    isinstance(piece_type, piece and \
                        piece.color == input_color):
                    return loc

        raise Exception("Piece not found: " + str(piece_type))

    def find_king(self, input_color):
        """
        Finds the Location of the King of input_color

        :type: input_color: Color
        :rtype: Location
        """
        return self.find_piece(King(input_color, Location(0, 0)))

    def get_king(self, input_color):
        """
        Returns King of input_color

        :type: input_color: Color
        :rtype: King
        """
        return self.piece_at_square(self.find_king(input_color))

    def remove_piece_at_square(self, location):
        """
        Removes piece at square

        :type: location: Location
        """
        self.position[location.rank][location.file] = None

    def place_piece_at_square(self, piece, location):
        """
        Places piece at given get_location

        :type: piece: Piece
        :type: location: Location
        """
        self.position[location.rank][location.file] = piece
        piece.location = location

    def move_piece(self, initial, final):
        """
        Moves piece from one location to another

        :type: initial: Location
        :type: final: Location
        """
        self.place_piece_at_square(self.piece_at_square(initial), final)
        self.remove_piece_at_square(initial)

    def update(self, move):
        """
        Updates position by applying selected move

        :type: move: Move
        """
        if move is None:
            raise Exception("Move cannot be None")

        if move.status == notation_const.KING_SIDE_CASTLE:
            self.move_piece(Location(move.end_loc.rank, 4), Location(move.end_loc.rank, 6))
            move.piece.get_location = Location(move.end_loc.rank, 6)
            self.move_piece(Location(move.end_loc.rank, 7), Location(move.end_loc.rank, 5))
            self.piece_at_square(Location(move.end_loc.rank, 5)).get_location = Location(move.end_loc.rank, 5)
            return

        if move.status == notation_const.QUEEN_SIDE_CASTLE:
            self.move_piece(Location(move.end_loc.rank, 4), Location(move.end_loc.rank, 2))
            move.piece.get_location = Location(move.end_loc.rank, 2)
            self.move_piece(Location(move.end_loc.rank, 0), Location(move.end_loc.rank, 3))
            self.piece_at_square(Location(move.end_loc.rank, 3)).get_location = Location(move.end_loc.rank, 3)
            return

        if type(move.piece) is Pawn:
            self.piece_at_square(move.start_loc).just_moved_two_steps = False

        if type(move.piece) is King or type(move.piece) is Rook:
            self.piece_at_square(move.start_loc).has_moved = True

        if move.status == notation_const.PROMOTE or \
                move.status == notation_const.CAPTURE_AND_PROMOTE:
            assert isinstance(move.piece, Pawn)

            self.move_piece(Location(move.start_rank, move.start_file), move.get_location())
            self.place_piece_at_square(move.promoted_to_piece, move.get_location())

        elif move.status == notation_const.EN_PASSANT:
            assert isinstance(move.piece, Pawn)

            self.move_piece(Location(move.start_rank, move.start_file), move.get_location())

            assert isinstance(self.piece_at_square(Location(move.start_rank, move.get_location().file)), Pawn)
            self.remove_piece_at_square(Location(move.start_rank, move.get_location().file))

        elif move.status == notation_const.MOVEMENT and \
            type(move.piece) is Pawn and \
                fabs(move.end_loc.rank - move.start_rank) == 2:
            move.piece.just_moved_two_steps = True
            self.move_piece(Location(move.start_rank, move.start_file), move.end_loc)

        else:
            self.move_piece(Location(move.start_rank, move.start_file), move.end_loc)
