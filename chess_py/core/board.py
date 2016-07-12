# -*- coding: utf-8 -*-


"""
Constructs board object which stores the location of all the pieces.

Default Array

[[0th row 0th item,  0th row 1st item,  0th row 2nd item],
 [1st row 0th item,  1st row 1st item,  1st row 2nd item],
 [2nd row 0th item, 2nd row 1st item,  2nd row 2nd item]]

Default board
8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ Black pieces
7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ Black pawns
6 ║a6… … … … … …h6
5 ║… … … … … … … …
4 ║… … … … … … … …
3 ║a3… … … … … …h3 Algebraic
2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ White pawns
1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ White pieces
-—╚═══════════════
——-a b c d e f g h

Pieces on the board are flipped so white home row is at index 0
and black home row is at index 7

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from __future__ import print_function
import copy
from math import fabs

from chess_py.core import color
from chess_py.core.algebraic import notation_const
from chess_py.core.algebraic.location import Location
from chess_py.core.color import Color
from chess_py.pieces.bishop import Bishop
from chess_py.pieces.king import King
from chess_py.pieces.pawn import Pawn
from chess_py.pieces.queen import Queen
from chess_py.pieces.rook import Rook
from chess_py.pieces.knight import Knight


class Board:
    """
    Standard starting position in a chess game.
    Initialized upon startup and is used when init_default constructor is used

    """
    # Initializes global variable to use when initializing default_position.
    white = color.white
    black = color.black

    default_position = [

        # First rank
        [Rook(Color(white), Location(0, 0)), Knight(Color(white), Location(0, 1)), Bishop(Color(white), Location(0, 2)),
         Queen(Color(white), Location(0, 3)), King(Color(white), Location(0, 4)), Bishop(Color(white), Location(0, 5)),
         Knight(Color(white), Location(0, 6)), Rook(Color(white), Location(0, 7))],

        # Second rank
        [Pawn(Color(white), Location(1, 0)), Pawn(Color(white), Location(1, 1)), Pawn(Color(white), Location(1, 2)),
         Pawn(Color(white), Location(1, 3)), Pawn(Color(white), Location(1, 4)), Pawn(Color(white), Location(1, 5)),
         Pawn(Color(white), Location(1, 6)), Pawn(Color(white), Location(1, 7))],

        # Third rank
        [None, None, None, None, None, None, None, None],

        # Fourth rank
        [None, None, None, None, None, None, None, None],

        # Fifth rank
        [None, None, None, None, None, None, None, None],

        # Sixth rank
        [None, None, None, None, None, None, None, None],

        # Seventh rank
        [Pawn(Color(black), Location(6, 0)), Pawn(Color(black), Location(6, 1)), Pawn(Color(black), Location(6, 2)),
         Pawn(Color(black), Location(6, 3)), Pawn(Color(black), Location(6, 4)), Pawn(Color(black), Location(6, 5)),
         Pawn(Color(black), Location(6, 6)), Pawn(Color(black), Location(6, 7))],

        # Eighth rank
        [Rook(Color(black), Location(7, 0)), Knight(Color(black), Location(7, 1)), Bishop(Color(black), Location(7, 2)),
         Queen(Color(black), Location(7, 3)), King(Color(black), Location(7, 4)), Bishop(Color(black), Location(7, 5)),
         Knight(Color(black), Location(7, 6)), Rook(Color(black), Location(7, 7))]
    ]

    def __init__(self, position):
        """
        Initializes 8 by 8 array of objects in file pawn.py to store a chess position.
        :type position: list
        """
        self.position = position

    @classmethod
    def init_default(cls):
        """
        Alternate init method for default starting position
        :rtype Board
        """
        return cls(cls.default_position)

    def piece_at_square(self, location):
        """
        Finds the chess piece at a square of the position.
        :type location Location
        :rtype Piece
        """
        return self.position[location.rank][location.file]

    def is_square_empty(self, location):
        """
        Finds whether a chess piece occupies a square of the position.
        :type location: Location
        :rtype bool
        """
        return self.position[location.rank][location.file] is None

    def unfiltered(self, input_color):
        """
        Returns list of all possible moves
        :type input_color Color
        :rtype list
        """
        moves = []

        # Loops through columns
        for row in self.position:

            # Loops through rows
            for piece in row:

                    # Tests if square on the board is not empty
                    if piece is not None and piece.color.equals(input_color):
                        # Adds all of piece's possible moves to moves list.
                        moves.extend(piece.possible_moves(self))

        return moves

    def all_possible_moves(self, input_color):
        """
        Filters list of moves and returns all legal moves
        :type input_color Color
        :rtype list
        """
        unfiltered = self.unfiltered(input_color)

        if not self.get_king(input_color).in_check(self):
            return unfiltered

        filtered = []

        for move in unfiltered:
            test = copy.deepcopy(self)
            test.update(move)
            if not test.get_king(input_color).in_check(test):
                filtered.append(move)

        return filtered

    def find_piece(self, piece):
        """
        Finds Location of the first piece that matches piece.
        If none is found, None is returned.
        :type piece Piece
        :rtype Location
        """
        for i in range(len(self.position)):

            for j in range(len(self.position)):
                loc = Location(i, j)
                if not self.is_square_empty(loc) and \
                        self.piece_at_square(loc).equals(piece):
                    return loc

        return None

    def find_king(self, input_color):
        """
        Finds the Location of the King of input_color
        :type input_color Color
        :rtype Location
        """
        return self.find_piece(King(input_color, Location(0, 0)))

    def get_king(self, input_color):
        """
        Returns King of input_color
        :type input_color Color
        :rtype King
        """
        return self.piece_at_square(self.find_king(input_color))

    def remove_piece_at_square(self, location):
        """
        Removes piece at square
        :type location: Location
        """
        self.position[location.rank][location.file] = None

    def place_piece_at_square(self, piece, location):
        """
        Places piece at given location
        :type piece pieces.Piece
        :type location Location
        """
        self.position[location.rank][location.file] = piece
        piece.location = location

    def move_piece(self, initial, final):
        """
        Moves piece from one location to another
        :type initial Location
        :type final Location
        """
        self.place_piece_at_square(self.piece_at_square(initial), final)
        self.remove_piece_at_square(initial)

    def update(self, move):
        """
        Updates position by applying selected move
        :type move Move
        """
        if move.status == notation_const.KING_SIDE_CASTLE:
            self.move_piece(Location(move.rank, 4), Location(move.rank, 6))
            move.piece.location = Location(move.rank, 6)
            self.move_piece(Location(move.rank, 7), Location(move.rank, 5))
            self.piece_at_square(Location(move.rank, 5)).location = Location(move.rank, 5)
            return

        if move.status == notation_const.QUEEN_SIDE_CASTLE:
            self.move_piece(Location(move.rank, 4), Location(move.rank, 2))
            move.piece.location = Location(move.rank, 2)
            self.move_piece(Location(move.rank, 0), Location(move.rank, 3))
            self.piece_at_square(Location(move.rank, 3)).location = Location(move.rank, 3)
            return

        if type(move.piece) is Pawn:
            move.piece.just_moved_two_steps = False

        if type(move.piece) is King or type(move.piece) is Rook:
            move.piece.has_moved = True

        if move.status == notation_const.PROMOTE or \
                move.status == notation_const.CAPTURE_AND_PROMOTE:
            assert isinstance(move.piece, Pawn)

            self.move_piece(Location(move.start_rank, move.start_file), move.end_location())
            self.place_piece_at_square(move.promoted_to_piece, move.end_location())

        elif move.status == notation_const.EN_PASSANT:
            assert isinstance(move.piece, Pawn)

            self.move_piece(Location(move.start_rank, move.start_file), move.end_location())

            assert isinstance(self.piece_at_square(Location(move.start_rank, move.end_location().file)), Pawn)
            self.remove_piece_at_square(Location(move.start_rank, move.end_location().file))

        elif move.status == notation_const.MOVEMENT and \
            type(move.piece) is Pawn and \
                fabs(move.end_location().rank - move.start_rank) == 2:
            move.piece.just_moved_two_steps = True
            self.move_piece(Location(move.start_rank, move.start_file), move.end_location())

        else:
            self.move_piece(Location(move.start_rank, move.start_file), move.end_location())

    def out(self):
        """
        Prints current position in console
        """
        # Loops through columns
        for i in range(len(self.position)):

            # Loops through rows
            for j in range(len(self.position[0])):

                # If there is a piece on the square
                if not self.is_square_empty(Location(7 - i, j)):

                    # Prints out symbol of piece
                    print(self.position[7 - i][j].symbol + " ", end="")
                else:
                    print("_ ", end="")
            print()

        print()
