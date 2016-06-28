"""
Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from setup import board
from setup.algebraic_notation import location
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King
from setup.algebraic_notation import notation_const
from setup.algebraic_notation.location import Location
from setup.algebraic_notation.move import Move


class Player:
    def __init__(self, color):
        """
        Creates interface for human player.
        :type color: color.Color
        """
        self.color = color

    def generate_move(self, position):
        """
        Returns valid and legal move given position
        :type position: board.Board
        """

        position.print()

        raw = str(input(self.color.string + "\'s move"))
        move = Converter(raw, self.color).get_move()

        while raw is not None and move.exit == 0:
            raw = str(input("Enter valid " + self.color.string + "\'s move"))
            move = Converter(raw, self.color).get_move()

        move = Converter(raw, self.color)

        return move
        # TODO eventually check move up against all_possible_moves

class Converter:
    def __init__(self, algebraic_string, input_color):
        """
        Default constructor for initializing a move using algebraic notation.

        pawn move e4
        piece move Nf3
        pawn capture exd5
        piece capture Qxf3
        Castle 00 or 000
        pawn promotion e8=Q

        :type algebraic_string: string
        :type input_color: color.Color
        """
        self.string = algebraic_string
        self.color = input_color
        self.status = notation_const.NOT_IMPLEMENTED
        self.start_file = None
        self.promoted_to_piece = None
        self.start_rank = None
        self.file = None
        self.rank = None
        self.piece = None
        self.exit = 0

        def set_rank(index):
            """
            Returns rank given index
            :type index: int
            :rtype int
            """
            return int(self.string[index]) - 1

        def set_file(index):
            """
            Returns file given index
            :type index: int
            :rtype int
            """
            return ord(self.string[index]) - 97

        def set_piece(index):
            """
            Returns specific piece given index of piece.
            :type index: int
            """
            if self.string[index].upper is 'R':
                return Rook(self.color, self.end_location())

            if self.string[index].upper is 'N':
                return Knight(self.color, self.end_location())

            if self.string[index].upper is 'B':
                return Bishop(self.color, self.end_location())

            if self.string[index].upper is 'Q':
                return Queen(self.color, self.end_location())

            if self.string[index].upper is 'K':
                return King(self.color, self.end_location())
            return None

        def init_kingside_castle():
            self.status = notation_const.KING_SIDE_CASTLE

        def init_queenside_castle():
            self.status = notation_const.QUEEN_SIDE_CASTLE

        def init_pawn_movement():
            """
            ex a4
            """
            self.file = set_file(0)
            self.rank = set_rank(1)
            self.piece = Pawn(self.color, self.end_location())
            self.status = notation_const.MOVEMENT

        def init_piece_movement():
            """
            ex Nf3
            """
            self.piece = set_piece(0)
            self.file = set_file(0)
            self.rank = set_file(1)
            self.status = notation_const.MOVEMENT

        def init_piece_capture():
            self.piece = set_piece(0)

            self.file = set_file(2)
            self.rank = set_rank(3)
            self.status = notation_const.CAPTURE

        def init_pawn_capture():
            self.piece = Pawn(self.color, self.end_location())
            self.start_file = set_file(0)

            self.file = set_file(2)
            self.rank = set_rank(3)
            self.status = notation_const.CAPTURE

        def init_pawn_promotion():
            """
            ex a8=Q
            """
            if self.would_move_be_promotion():
                self.file = set_file(0)
                self.rank = set_rank(1)
                self.piece = Pawn(self.color, self.end_location())
                self.status = notation_const.PROMOTE
                self.promoted_to_piece = set_piece(3)

        def init_piece_movement_file():
            """
            ex aRa3
            """
            self.start_file = set_file(0)
            self.piece = set_piece(1)
            self.file = set_file(2)
            self.rank = set_rank(3)
            self.status = notation_const.MOVEMENT

        def init_piece_movement_rank_file():
            """
            ex a4Rd4
            """
            self.start_file = set_file(0)
            self.start_rank = set_rank(1)
            self.piece = set_piece(2)
            self.file = set_file(3)
            self.rank = set_rank(4)
            self.status = notation_const.MOVEMENT

        def init_pawn_promotion_capture():
            """
            exd8=Q
            """
            if self.would_move_be_promotion():
                self.start_file = set_rank(0)
                self.file = set_file(2)
                self.rank = set_rank(3)
                self.piece = Pawn(self.color, self.end_location())
                self.status = notation_const.PROMOTE
                self.promoted_to_piece = set_piece(5)
            else:
                self.exit = 1
                print("Not a promotion")

        # King side castle
        if algebraic_string == "00":
            init_kingside_castle()

        # Queen side castle
        elif algebraic_string == "000":
            init_queenside_castle()

        # Pawn movement
        elif len(algebraic_string) == 2:
            init_pawn_movement()

        # Non-pawn Piece movement
        elif len(algebraic_string) == 3:
            init_piece_movement()

        elif len(algebraic_string) == 4:

            # Capture
            if algebraic_string[1].upper() == "X":
                """
                ex Nxf3
                """
                # If this is a pawn capture
                if not algebraic_string[0].isupper():
                    init_pawn_capture()
                else:
                    init_piece_capture()

            # Pawn Promotion
            elif algebraic_string[2] == "=":
                init_pawn_promotion()

            # Non-pawn Piece movement with file specified
            elif algebraic_string[1].isupper():
                init_piece_movement_file()

        elif len(algebraic_string) == 5:

            # Non-pawn Piece movement with rank and file specified
            if algebraic_string[2].isupper():
                init_piece_movement_rank_file()

        elif len(algebraic_string) == 6:

            # Pawn promote with capture
            init_pawn_promotion_capture()

        else:
            self.exit = 1
        self.validate()

    def get_move(self):
        move = Move.init_manual(self.rank, self.file, self.piece, self.status)
        move.start_file = self.start_file
        move.start_rank = self.start_rank
        move.string = self.string
        move.promoted_to_piece = self.promoted_to_piece
        move.exit = self.exit
        return move

    def validate(self):
        self.exit = self.end_location().exit

    def equals(self, move):
        """
        Finds if move is same move as this one.
        :type move: algebraic.Move
        """
        return self.rank == move.rank and self.file == move.file and self.piece.equals(
            move.piece) and self.status == move.status and self.color == move.color and self.start_file == move.start_file and self.start_rank == move.start_rank

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

    def would_move_be_promotion(self):
        """
        Finds if move from current location
        """
        if self.rank == 0 and self.color == color.black:
            return True
        elif self.rank == 7 and self.color == color.white:
            return True
        return False

