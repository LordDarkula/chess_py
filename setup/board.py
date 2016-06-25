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

from pieces import bishop, king, knight, pawn, queen, rook
from setup import color
from setup.algebraic_notation import algebraic


class Board:
    """
    Standard starting position in a chess game.
    Initialized upon startup and is used when init_default constructor is used

    """
        # First rank
    default_position = \
        [[rook.Rook(color.Color(True), algebraic.Location(0, 0)), knight.Knight(color.Color(True), algebraic.Location(0, 1)), bishop.Bishop(color.Color(True), algebraic.Location(0, 2)), queen.Queen(
            color.Color(True), algebraic.Location(0, 3)),
          king.King(color.Color(True), algebraic.Location(0, 4)), bishop.Bishop(color.Color(True), algebraic.Location(0, 5)), knight.Knight(color.Color(True), algebraic.Location(0, 6)), rook.Rook(
                color.Color(True), algebraic.Location(0, 7))],
         # Second rank
         [pawn.Pawn(color.Color(True), algebraic.Location(1, 0)), pawn.Pawn(color.Color(True), algebraic.Location(1, 1)), pawn.Pawn(color.Color(True), algebraic.Location(1, 2)), pawn.Pawn(
             color.Color(True), algebraic.Location(1, 3)), pawn.Pawn(color.Color(True), algebraic.Location(1, 4)),
          pawn.Pawn(color.Color(True), algebraic.Location(1, 5)), pawn.Pawn(color.Color(True), algebraic.Location(1, 6)), pawn.Pawn(color.Color(True), algebraic.Location(1, 7))],
         # Third rank
         [None, None, None, None, None, None, None, None],
         # Fourth rank
         [None, None, None, None, None, None, None, None],
         # Fifth rank
         [None, None, None, None, None, None, None, None],
         # Sixth rank
         [None, None, None, None, None, None, None, None],
         # Seventh rank
         [pawn.Pawn(color.Color(False), algebraic.Location(6, 0)), pawn.Pawn(color.Color(False), algebraic.Location(6, 1)), pawn.Pawn(color.Color(False), algebraic.Location(6, 2)), pawn.Pawn(
             color.Color(False), algebraic.Location(6, 3)), pawn.Pawn(color.Color(False), algebraic.Location(6, 4)),
          pawn.Pawn(color.Color(False), algebraic.Location(6, 5)), pawn.Pawn(color.Color(False), algebraic.Location(6, 6)), pawn.Pawn(color.Color(False), algebraic.Location(6, 7))],
         # Eighth rank
         [rook.Rook(color.Color(False), algebraic.Location(7, 0)), knight.Knight(color.Color(False), algebraic.Location(7, 1)), bishop.Bishop(color.Color(False), algebraic.Location(7, 2)), queen.Queen(
             color.Color(False), algebraic.Location(7, 3)),
          king.King(color.Color(False), algebraic.Location(7, 4)), bishop.Bishop(color.Color(False), algebraic.Location(7, 5)), knight.Knight(color.Color(False), algebraic.Location(7, 6)), rook.Rook(
             color.Color(False), algebraic.Location(7, 7))]]

    def __init__(self, position):
        """
        Initializes 8 by 8 array of objects in file pawn.py to store a chess position.
        :type self: board.Board
        :type position: list
        """
        self.position = position

    @classmethod
    def init_default(cls):
        """
        Alternate init method for default starting position
        :return: board.Board
        """
        return cls(cls.default_position)

    def piece_at_square(self, location):
        """
        Finds the chess piece at a square of the position.
        :type location algebraic.Location
        :rtype pieces.Piece
        """
        return self.position[location.rank][location.file]

    def is_square_empty(self, location):
        """
        Finds whether a chess piece occupies a square of the position.
        :type location: algebraic.Location
        :rtype bool
        """
        return self.position[location.rank][location.file] is None

    def all_possible_moves(self):
        """
        Returns list of all possible moves
        :rtype list
        """
        moves = []

        # Loops through columns
        for i in range(len(self.position)):

            # Loops through rows
            for j in range(len(self.position[0])):

                    # Tests if square on the board is not empty
                    if not self.is_square_empty(algebraic.Location(i, j)):

                        # Adds all of piece's possible moves to moves list.
                        moves.extend(self.piece_at_square(algebraic.Location(i, j)).possible_moves())

        return moves

    def print(self):
        """
        Prints current position in console
        """
        # Loops through columns
        for i in range(len(self.position)):

            # Loops through rows
            for j in range(len(self.position[0])):

                # If there is a piece on the square
                if not self.is_square_empty(algebraic.Location(i, j)):

                    # Prints out symbol of piece
                    print(self.position[i][j].symbol + " ", end="")
                else:
                    print("_ ", end="")
            print()

        print()