from core.algebraic.location import Location
from core.algebraic import notation_const
from core import color


class Move:
    string = None
    color = None
    file = None
    rank = None

    status = notation_const.NOT_IMPLEMENTED
    start_rank = None
    start_file = None
    promoted_to_piece = None

    piece = None
    exit = 0

    def __init__(self, location, piece, status, start_rank=None, start_file=None):
        """
        Alternate constructor to create move using object algebraic.Location
        :type location: algebraic.Location
        :type piece: Piece
        :type status: int
        """
        if self.on_board:
            self.rank = location.rank
            self.file = location.file
            self.status = status
            self.piece = piece
            self.color = piece.color

            self.start_rank = start_rank
            self.start_file = start_file
        else:
            self.exit = 1

    @classmethod
    def init_manual(cls, rank, file, piece, status, start_rank=None, start_file=None):
        """
        Alternate constructor to create move using integer location
        :type rank: int
        :type file: int
        :type piece: Piece
        :type status int
        :type start_rank int
        :type start_file int
        """
        if cls.on_board:
            cls.rank = rank
            cls.file = file
            cls.status = status
            cls.piece = piece
            cls.color = piece.color
            cls.start_rank = start_rank
            cls.start_file = start_file
            return cls
        else:
            cls.exit = 1
            return cls

    def validate(self):
        self.exit = self.end_location().exit

    def equals(self, move):
        """
        Finds if move is same move as this one.
        :type move: algebraic.Move
        """
        return self.rank == move.rank and \
            self.file == move.file and \
            self.piece.equals(move.piece) and \
            self.status == move.status and \
            self.color == move.color and \
            self.start_file == move.start_file and \
            self.start_rank == move.start_rank

    def on_board(self):
        """
        Determines whether move exists.
        :rtype bool
        """
        return self.end_location().on_board()

    def end_location(self):
        """
        Finds end location for move.
        :rtype Location
        """
        return Location(self.rank, self.file)

    def would_move_be_promotion(self):
        """
        Finds if move from current location
        """
        if self.rank == 0 and \
                self.color == color.black:
            return True
        elif self.rank == 7 and \
                self.color == color.white:
            return True

        return False

    def print(self):
        print(self.piece.symbol, " Rank: ", self.rank, " File:  ", self.file, " Status: ", self.status)
