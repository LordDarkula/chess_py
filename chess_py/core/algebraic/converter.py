# -*- coding: utf-8 -*-

"""
Methods that take external input and attempt
to turn them into usable commands.

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from .. import color
from . import notation_const
from .location import Location
from .move import Move
from ...pieces.bishop import Bishop
from ...pieces.king import King
from ...pieces.pawn import Pawn
from ...pieces.queen import Queen
from ...pieces.rook import Rook
from ...pieces.knight import Knight


def incomplete_alg(algebraic_string, input_color):
    """
    Converts a string written in short algebraic form into an incomplete move.
    These incomplete moves do not have the initial location specified and
    therefore cannot be used to update the board. IN order to fully utilize
    incomplete move, it must be run through ``make_legal()`` with
    the corresponding position. It is recommended to use
    ``short_alg()`` instead of this method because it returns a complete
    move.

    Examples: e4, Nf3, exd5, Qxf3, 00, 000, e8=Q

    :type: algebraic_string: str
    :type: input_color: Color
    """
    def edge_rank():
        if input_color == color.white:
            return 0

        return 7

    def set_rank(index):
        """
        Returns rank given index

        :type: index: int
        :rtype: int
        """
        return int(algebraic_string[index]) - 1

    def set_file(index):
        """
        Returns file given index

        :type: index: int
        :rtype: int
        """
        return ord(algebraic_string[index]) - 97

    def set_piece(index, loc):
        """
        Returns specific piece given index of piece.

        :type: index: int
        :type: loc Location
        """
        piece = algebraic_string[index].strip()
        piece = piece.upper()

        if piece == 'R':
            return Rook(input_color, loc)

        if piece == 'N':
            return Knight(input_color, loc)

        if piece == 'B':
            return Bishop(input_color, loc)

        if piece == 'Q':
            return Queen(input_color, loc)

        if piece == 'K':
            return King(input_color, loc)
        return None

    end_loc = Location(edge_rank(), 6)
    edge_rank = edge_rank()

    is_kingside = algebraic_string == "00"
    is_queenside = algebraic_string == "000"

    # King side castle
    if is_kingside:
        return Move(end_loc,
                    piece=King(input_color, Location(edge_rank, 4)),
                    status=notation_const.KING_SIDE_CASTLE,
                    start_rank=edge_rank,
                    start_file=4)

    # Queen side castle
    if is_queenside:
        end_loc = Location(edge_rank, 2)
        move = Move(end_loc=end_loc,
                    piece=King(input_color, Location(edge_rank, 4)),
                    status=notation_const.QUEEN_SIDE_CASTLE,
                    start_rank=edge_rank,
                    start_file=4)

        return move

    pawn_movement = len(algebraic_string) == 2
    piece_movement = len(algebraic_string) == 3

    # Pawn movement
    if pawn_movement:
        end_loc = Location(set_rank(1), set_file(0))

        return Move(end_loc=end_loc,
                    piece=Pawn(input_color, end_loc),
                    status=notation_const.MOVEMENT)

    # Non-pawn Piece movement
    if piece_movement:
        end_loc = Location(set_rank(2), set_file(1))
        if set_piece(0, end_loc) is not None:
            return Move(end_loc=end_loc,
                        piece=set_piece(0, end_loc),
                        status=notation_const.MOVEMENT)
        else:
            return None

    # Multiple options
    if len(algebraic_string) == 4:

        capture = algebraic_string[1].upper() == "X"

        # Capture
        if capture:

            pawn_capture = not algebraic_string[0].isupper()
            piece_capture = algebraic_string[0].isupper()
            pawn_promotion = algebraic_string[2] == "="
            file_specified = algebraic_string[1].isupper()

            """
            ex Nxf3
            """
            # If this is a pawn capture
            if pawn_capture:
                end_loc = Location(set_rank(3), set_file(2))
                return Move(end_loc=end_loc,
                            piece=Pawn(input_color, end_loc),
                            status=notation_const.CAPTURE,
                            start_file=set_file(0))

            # If this is a piece capture
            elif piece_capture:
                end_loc = Location(set_rank(3), set_file(2))
                return Move(end_loc=end_loc,
                            piece=set_piece(0, end_loc),
                            status=notation_const.CAPTURE)

            # Pawn Promotion
            elif pawn_promotion:
                end_loc = Location(set_rank(1), set_file(0))
                return Move(end_loc=end_loc,
                            piece=Pawn(input_color, end_loc),
                            status=notation_const.PROMOTE,
                            promoted_to_piece=set_piece(3, end_loc))

            # Non-pawn Piece movement with file specified
            elif file_specified:
                end_loc = Location(set_rank(3), set_file(2))
                return Move(end_loc=end_loc,
                            piece=set_piece(1, end_loc),
                            status=notation_const.MOVEMENT,
                            start_file=set_file(0))

            else:
                return None

    # Multiple options
    if len(algebraic_string) == 5:

        rank_file_specified = algebraic_string[2].isupper()

        # Non-pawn Piece movement with rank and file specified
        if rank_file_specified:
            end_loc = Location(set_rank(4), set_file(3))
            return Move(end_loc=end_loc,
                        piece=set_piece(2, end_loc),
                        status=notation_const.MOVEMENT,
                        start_file=set_file(0),
                        start_rank=set_rank(1))

    pawn_promote_capture = len(algebraic_string) == 6

    if pawn_promote_capture:
        """
        exd8=Q
        """
        # Pawn promote with capture
        end_loc = Location(set_rank(3), set_file(2))
        return Move(end_loc=end_loc,
                    piece=Pawn(input_color, end_loc),
                    status=notation_const.MOVEMENT,
                    start_file=set_file(0),
                    promoted_to_piece=set_piece(5, end_loc))

    return None


def make_legal(move, position):
    """
    Converts an incomplete move (initial ``Location`` not specified)
    and the corresponding position into the a complete move
    with the most likely starting point specified. If no moves match, ``None``
    is returned.

    :type: move: Move
    :type: position: Board
    :rtype: Move
    """
    assert isinstance(move, Move)
    for test_move in position.all_possible_moves(move.color):

        if move.status == notation_const.START_LOC_SPECIFIED:
            if move.end_loc == test_move.end_loc and \
                            move.start_rank == test_move.start_rank and \
                            move.start_file == test_move.start_file:
                return test_move
            else:
                continue

        if move == test_move:
            return test_move

    return None


def short_alg(algebraic_string, input_color, position):
    """
    Converts a string written in short algebraic form, the color
    of the side whose turn it is, and the corresponding position
    into a complete move that can be played. If no moves match,
    None is returned.

    Examples: e4, Nf3, exd5, Qxf3, 00, 000, e8=Q

    :type: algebraic_string: str
    :type: input_color: Color
    :type: position: Board
    """
    return make_legal(incomplete_alg(algebraic_string, input_color), position)

def long_alg(alg_str, position):
    """
    Converts a string written in long algebraic form
    and the corresponding position into a complete move
    (initial location specified). Used primarily for
    UCI, but can be used for other purposes.

    :type: alg_str: str
    :type: position: Board
    :rtype: Move
    """
    end = Location.init_alg(alg_str[2] + alg_str[3])
    start = Location.init_alg(alg_str[0] + alg_str[1])

    if position.piece_at_square(start) is not None:
        piece = position.piece_at_square(start)
    else:
        raise Exception("Invalid move input")

    pr_piece = None
    if len(alg_str) == 5:
        if alg_str[4] == "Q":
            pr_piece = Queen(piece.color, end)
        elif alg_str[4] == "R":
            pr_piece = Rook(piece.color, end)
        elif alg_str[4] == "B":
            pr_piece = Bishop(piece.color, end)
        elif alg_str[4] == "N":
            pr_piece = Knight(piece.color, end)
        else:
            raise Exception("Invalid move input")

    return make_legal(Move(end_loc=end,
                           piece=piece,
                           status=notation_const.START_LOC_SPECIFIED,
                           start_rank=start.rank,
                           start_file=start.file,
                           promoted_to_piece=pr_piece), position)
