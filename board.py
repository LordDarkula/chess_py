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
"""

from pieces import pawn
from pieces import knight
from pieces import bishop
from pieces import rook
from pieces import queen
from pieces import king


class Board:
    """
    Standard starting position in a chess game.
    Initialized upon startup and can be accessed with the keyword "default"

    """
    # First rank
    default_position = \
        [[rook.Rook("white"), knight.Knight("white"), bishop.Bishop("white"), queen.Queen("white"),
          king.King("white"), bishop.Bishop("white"), knight.Knight("white"), rook.Rook("white")],
         # Second rank
         [pawn.Pawn("white"), pawn.Pawn("white"), pawn.Pawn("white"), pawn.Pawn("white"), pawn.Pawn("white"),
          pawn.Pawn("white"), pawn.Pawn("white"), pawn.Pawn("white")],
         # Third rank
         [None, None, None, None, None, None, None, None],
         # Fourth rank
         [None, None, None, None, None, None, None, None],
         # Fifth rank
         [None, None, None, None, None, None, None, None],
         # Sixth rank
         [None, None, None, None, None, None, None, None],
         # Seventh rank
         [pawn.Pawn("black"), pawn.Pawn("black"), pawn.Pawn("black"), pawn.Pawn("black"), pawn.Pawn("black"),
          pawn.Pawn("black"), pawn.Pawn("black"), pawn.Pawn("black")],
         # Eighth rank
         [rook.Rook("black"), knight.Knight("black"), bishop.Bishop("black"), queen.Queen("black"),
          king.King("black"), bishop.Bishop("black"), knight.Knight("black"), rook.Rook("black")]]

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
        :return:
        """
        cls.position = cls.default_position

    def piece_at_square(self, location):

        """
        Finds the chess piece at a square of the position.
        :param self: list
        :type location: algebraic.Location
        :rtype pieces *
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


"""
    def move(self, move):



        :type move: object

        if type(move.piece) is pieces.Pawn and move.piece.white == True:

            if

"""
