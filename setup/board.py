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
        [[rook.Rook(color.Color(True)), knight.Knight(color.Color(True)), bishop.Bishop(color.Color(True)), queen.Queen(
            color.Color(True)),
          king.King(color.Color(True)), bishop.Bishop(color.Color(True)), knight.Knight(color.Color(True)), rook.Rook(
                color.Color(True))],
         # Second rank
         [pawn.Pawn(color.Color(True)), pawn.Pawn(color.Color(True)), pawn.Pawn(color.Color(True)), pawn.Pawn(
             color.Color(True)), pawn.Pawn(color.Color(True)),
          pawn.Pawn(color.Color(True)), pawn.Pawn(color.Color(True)), pawn.Pawn(color.Color(True))],
         # Third rank
         [None, None, None, None, None, None, None, None],
         # Fourth rank
         [None, None, None, None, None, None, None, None],
         # Fifth rank
         [None, None, None, None, None, None, None, None],
         # Sixth rank
         [None, None, None, None, None, None, None, None],
         # Seventh rank
         [pawn.Pawn(color.Color(False)), pawn.Pawn(color.Color(False)), pawn.Pawn(color.Color(False)), pawn.Pawn(
             color.Color(False)), pawn.Pawn(color.Color(False)),
          pawn.Pawn(color.Color(False)), pawn.Pawn(color.Color(False)), pawn.Pawn(color.Color(False))],
         # Eighth rank
         [rook.Rook(color.Color(False)), knight.Knight(color.Color(False)), bishop.Bishop(color.Color(False)), queen.Queen(
             color.Color(False)),
          king.King(color.Color(False)), bishop.Bishop(color.Color(False)), knight.Knight(color.Color(False)), rook.Rook(
             color.Color(False))]]

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
        :param self: list
        :type location: algebraic.Location
        :rtype Pawn.pawn, Knight.knight, Bishop.bishop, Rook.rook, Queen.queen, King.king
        """
        return self.position[location.rank][location.file]

    def is_square_empty(self, location):
        """
        Finds whether a chess piece occupies a square of the position.
        :param self: 2D 8 by 8 list occupied by objects in pawn.py
        :type location: algebraic.Location
        :rtype bool
        """
        return self.position[location.rank][location.file] is None

    def all_possible_moves(self):
        """
        Returns list of all possible moves
        :return: list
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

# TODO add method all_possible_moves
