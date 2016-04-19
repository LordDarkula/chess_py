"""
Contains all classes that store and manipulate algebraic notation.
All algebraic inputs are converted and stored internally as . . .

rank and file - integers from 0 to 7
piece - object in "pieces.py"
color - used for identifying which color piece to initialize

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

from pieces import pawn
from pieces import knight
from pieces import bishop
from pieces import rook
from pieces import queen
from pieces import king


class Location:
    def __init__(self, rank, file):

        """
        Creates a location on a chessboard given x and y coordinates.
        :type rank: int
        :type file: int
        """

        if -1 < rank < 8 and -1 < file < 8:
            self.rank = rank
            self.file = file
        else:
            self.rank = None
            self.file = None
            print("Cannot create location not on board")

    def shift_up(self):

        """
        Finds Location shifted up by 1
        :rtype: algebraic.Location
        """
        if self.rank < 7:
            return Location(self.rank + 1, self.file)
        else:
            print("Cannot move up off the board")
            return None

    def shift_down(self):

        """
        Finds Location shifted down by 1
        :rtype: algebraic.Location
        """
        if self.rank > 0:
            return Location(self.rank - 1, self.file)
        else:
            print("Cannot move down off the board")
            return None

    def shift_right(self):

        """
        Finds Location shifted right by 1
        :rtype: algebraic.Location
        """
        if self.file < 7:
            return Location(self.rank, self.file + 1)
        else:
            print("Cannot move right off the board")
            return None

    def shift_left(self):

        """
        Finds Location shifted left by 1
        :rtype: algebraic.Location
        """
        if self.file > 0:
            return Location(self.rank, self.file - 1)
        else:
            print("Cannot move left off the board")
            return None

    def shift_up_right(self):
        """
        Finds Location shifted right by 1
        :rtype: algebraic.Location
        """
        if self.rank < 7 and self.file < 7:
            return self.shift_up().shift_right()
        else:
            print("Cannot move up and right off the board")

        #TODO add method that checks if location is valid

class Move:
    def __init__(self, algebraic_string, color):

        """
        Default constructor for initializing a move using algebraic notation.

        pawn move e4
        piece move Nf3
        pawn capture exd5
        piece capture Qxf3
        Castle 00 or 000
        pawn promotion e8=Q

        :type algebraic_string: string
        :type color: color.Color
        """
        if len(algebraic_string) == 2:

            """
            ex a4
            """
            self.file = ord(algebraic_string[0]) - 97
            self.rank = int(algebraic_string[1]) - 1
            self.piece = pawn.Pawn(color)

        elif len(algebraic_string) == 3:
            """
            ex Nf3
            """
            if algebraic_string[0] is 'R':
                self.piece = rook.Rook(color)

            if algebraic_string[0] is 'N':
                self.piece = knight.Knight(color)

            if algebraic_string[0] is 'B':
                self.piece = bishop.Bishop(color)

            if algebraic_string[0] is 'Q':
                self.piece = queen.Queen(color)

            if algebraic_string[0] is 'K':
                self.piece = king.King(color)






            self.file = ord(algebraic_string[0]) - 97
            self.rank = int(algebraic_string[1]) - 1

        #TODO elif:
            """
            Two cases:
            case 1: capture
            ex
            case 2: specify which of duplicate piece made move
            """
        else:
            print("Invalid Move")
            self.rank = None
            self.file = None
        #TODO add method that checks if move is valid
    @classmethod
    def init_manual(cls, rank, file, piece):

        """
        Alternate constructor to create move using integer location
        :type rank: int
        :type file: int
        :type piece: pieces *
        """
        if -1 < rank < 8 and -1 < file < 8:
            cls.rank = rank
            cls.file = file
        else:
            print("Cannot create move not on board")
            cls.rank = None
            cls.file = None
        cls.piece = piece


