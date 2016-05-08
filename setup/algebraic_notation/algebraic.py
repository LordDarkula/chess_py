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

from pieces import pawn, knight, bishop, rook, queen, king
from setup.algebraic_notation import special_notation_constants


class Location:
    def __init__(self, rank, file):
        """
        Creates a location on a chessboard given x and y coordinates.
        :type rank: int
        :type file: int
        """

        if self.on_board():
            self.rank = rank
            self.file = file
        else:
            self.rank = None
            self.file = None
            print("Cannot create location not on board")

    def equals(self, location):
        """
        Finds is location on board is the same as current equation.
        :type location: algebraic.Location
        """
        return location.not_none() and self.rank == location.rank and self.file == location.file

    def on_board(self):
        """
        Returns if the move is on the board or not.
        :rtype bool
        """
        if self.rank is not None and self.file is not None and -1 < self.rank < 8 and -1 < self.file < 8:
            return True
        else:
            return False

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
        Finds Location shifted up right by 1
        :rtype: algebraic.Location
        """
        if self.rank < 7 and self.file < 7:
            return self.shift_up().shift_right()
        else:
            print("Cannot move up and right off the board")

    def shift_up_left(self):
        """
        Finds Location shifted up left by 1
        :rtype: algebraic.Location
        """
        if self.rank < 7 and self.file > 1:
            return self.shift_up().shift_left()
        else:
            print("Cannot move up and left off the board")

    def not_none(self):
        """
        Determines whether location exists.
        :rtype bool
        """
        return self is not None and self.rank is not None and self.file is not None and self.on_board()

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
        self.color = color
        if algebraic_string == "00":
            self.status = special_notation_constants.KING_SIDE_CASTLE

        elif algebraic_string == "000":
            self.status = special_notation_constants.QUEEN_SIDE_CASTLE

        elif len(algebraic_string) == 2:
            """
            ex a4
            """
            self.file = ord(algebraic_string[0]) - 97
            self.rank = int(algebraic_string[1]) - 1
            self.piece = pawn.Pawn(color)
            self.status = special_notation_constants.MOVEMENT

        elif len(algebraic_string) == 3:
            """
            ex Nf3
            """
            self.piece = self.set_piece(algebraic_string, 0)
            self.file = ord(algebraic_string[0]) - 97
            self.rank = int(algebraic_string[1]) - 1
            self.status = special_notation_constants.MOVEMENT

        elif len(algebraic_string) == 4:

            if algebraic_string[1].upper() == "X":
                """
                ex Nxf3
                """
                self.piece = self.set_piece(algebraic_string, 0)
                self.file = ord(algebraic_string[0]) - 97
                self.rank = int(algebraic_string[1]) - 1
                self.status = special_notation_constants.CAPTURE #TODO add promote and capture 

            elif algebraic_string[2] == "=":
                """
                ex a8=Q
                """
                self.file = ord(algebraic_string[0]) - 97
                self.rank = int(algebraic_string[1]) - 1
                self.piece = pawn.Pawn(color)
                self.status = special_notation_constants.PROMOTE
                self.promoted_to_piece = self.set_piece(algebraic_string, 3)

            else:
                self.start_rank = ord(algebraic_string[0]) - 97
                self.set_piece(algebraic_string, color, 1)
                self.file = ord(algebraic_string[0]) - 97
                self.rank = int(algebraic_string[1]) - 1
                self.status = special_notation_constants.MOVEMENT

            """
            Two cases:
            case 1: capture
            ex
            case 2: specify which of duplicate piece made move
            """
        else:
            print("Invalid Move")
            self.make_location_none()

    # TODO add method that checks if move is valid

    @classmethod
    def init_with_location(cls, location, piece, status):
        """
        Alternate constructor to create move using object algebraic.Location
        :type location: algebraic.Location
        :type piece: pieces *
        :type status: int
        """
        if cls.on_board:
            cls.rank = location.rank
            cls.file = location.file
            cls.status = status
        else:
            print("Cannot create move not on board")
            cls.rank = None
            cls.file = None
        cls.piece = piece

    @classmethod
    def init_manual(cls, rank, file, piece, status):
        """
        Alternate constructor to create move using integer location
        :type rank: int
        :type file: int
        :type piece: Pawn.pawn, Knight.knight, Bishop.bishop, Rook.rook, Queen.queen, King.king
        :type status int
        """
        if cls.on_board:
            cls.rank = rank
            cls.file = file
            cls.status = status
        else:
            print("Cannot create move not on board")
            cls.rank = None
            cls.file = None
        cls.piece = piece

    def equals(self, move):
        """
        Finds if move is same move as this one.
        :type move: algebraic.Move
        """
        return move.not_none() and self.rank == move.rank and self.file == move.file and self.piece.equals(
            move.piece) and self.status == move.status

    def set_piece(self, algebraic_string, index):
        """
        Creates specific piece given raw move, color, and index of piece.
        :type algebraic_string: basestring
        :type index: int
        """
        if algebraic_string[index].upper is 'R':
            return rook.Rook(self.color)

        if algebraic_string[index].upper is 'N':
            return knight.Knight(self.color)

        if algebraic_string[index].upper is 'B':
            return bishop.Bishop(self.color)

        if algebraic_string[index].upper is 'Q':
            return queen.Queen(self.color)

        if algebraic_string[index].upper is 'K':
            return king.King(self.color)
        return None

    def on_board(self):
        """
        Determines whether move exists.
        :rtype bool
        """
        if self.rank is not None and self.file is not None and -1 < self.rank < 8 and -1 < self.file < 8:
            return True
        else:
            return False

    def end_location(self):
        """
        Finds end location for move.
        :rtype Location
        """
        return Location(self.rank, self.file)

    def make_location_none(self):
        self.rank = None
        self.file = None

    def not_none(self):
        """
        Determines whether location exists.
        :rtype bool
        """
        return self is not None and self.rank is not None and self.file is not None and self.on_board()