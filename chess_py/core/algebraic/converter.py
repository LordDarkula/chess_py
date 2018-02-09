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


def _get_piece(string, index):
    """
    Returns Piece subclass given index of piece.

    :type: index: int
    :type: loc Location
    """
    piece = string[index].strip()
    piece = piece.upper()

    piece_dict = {'R': Rook,
                  'P': Pawn,
                  'B': Bishop,
                  'N': Knight,
                  'Q': Queen,
                  'K': King}

    return piece_dict.get(piece, None)


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

    def get_rank(index):
        """
        Returns rank given index

        :type: index: int
        :rtype: int
        """
        return int(algebraic_string[index]) - 1

    def get_file(index):
        """
        Returns file given index

        :type: index: int
        :rtype: int
        """
        return ord(algebraic_string[index]) - 97

    end_loc = Location(edge_rank(), 6)
    edge_rank = edge_rank()

    is_kingside = algebraic_string in ["00", "oo", "OO", "0-0", "o-o", "O-O"]
    is_queenside = algebraic_string in ["000", "ooo", "OOO", "0-0-0", "o-o-o", "O-O-O"]

    if algebraic_string is None or len(algebraic_string) <= 1:
        return None

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
        end_loc = Location(get_rank(1), get_file(0))

        return Move(end_loc=end_loc,
                    piece=Pawn(input_color, end_loc),
                    status=notation_const.MOVEMENT)

    # Non-pawn Piece movement
    if piece_movement:
        end_loc = Location(get_rank(2), get_file(1))
        if _get_piece(algebraic_string, 0) is not None:
            return Move(end_loc=end_loc,
                        piece=_get_piece(algebraic_string, 0)(input_color, end_loc),
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
                end_loc = Location(get_rank(3), get_file(2))
                return Move(end_loc=end_loc,
                            piece=Pawn(input_color, end_loc),
                            status=notation_const.CAPTURE,
                            start_file=get_file(0))

            # If this is a piece capture
            elif piece_capture:
                end_loc = Location(get_rank(3), get_file(2))
                return Move(end_loc=end_loc,
                            piece=_get_piece(algebraic_string, 0)(input_color, end_loc),
                            status=notation_const.CAPTURE)

            # Pawn Promotion
            elif pawn_promotion:
                end_loc = Location(get_rank(1), get_file(0))
                return Move(end_loc=end_loc,
                            piece=Pawn(input_color, end_loc),
                            status=notation_const.PROMOTE,
                            promoted_to_piece=_get_piece(algebraic_string, 3)(input_color, end_loc))

            # Non-pawn Piece movement with file specified
            elif file_specified:
                end_loc = Location(get_rank(3), get_file(2))
                return Move(end_loc=end_loc,
                            piece=_get_piece(algebraic_string, 1)(input_color, end_loc),
                            status=notation_const.MOVEMENT,
                            start_file=get_file(0))

            else:
                return None

    # Multiple options
    if len(algebraic_string) == 5:

        rank_file_specified = algebraic_string[2].isupper()

        # Non-pawn Piece movement with rank and file specified
        if rank_file_specified:
            end_loc = Location(get_rank(4), get_file(3))
            return Move(end_loc=end_loc,
                        piece=_get_piece(algebraic_string, 2)(input_color, end_loc),
                        status=notation_const.MOVEMENT,
                        start_file=get_file(0),
                        start_rank=get_rank(1))

    pawn_promote_capture = len(algebraic_string) == 6

    if pawn_promote_capture:
        """
        exd8=Q
        """
        # Pawn promote with capture
        end_loc = Location(get_rank(3), get_file(2))
        return Move(end_loc=end_loc,
                    piece=Pawn(input_color, end_loc),
                    status=notation_const.MOVEMENT,
                    start_file=get_file(0),
                    promoted_to_piece=_get_piece(algebraic_string, 5)(input_color, end_loc))

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
    end = Location.init_alg(alg_str[2:])
    start = Location.init_alg(alg_str[:2])
    piece = position.piece_at_square(start)

    if piece is None:
        raise Exception("Invalid move input")

    if len(alg_str) == 4:
        return make_legal(Move(end_loc=end,
                               piece=piece,
                               status=notation_const.START_LOC_SPECIFIED,
                               start_rank=start.rank,
                               start_file=start.file), position)

    promoted_to = _get_piece(alg_str, 4)
    if promoted_to is None or isinstance(promoted_to, King) or isinstance(promoted_to, Pawn):
        raise Exception("Invalid move input")

    return make_legal(Move(end_loc=end,
                           piece=piece,
                           status=notation_const.START_LOC_SPECIFIED,
                           start_rank=start.rank,
                           start_file=start.file,
                           promoted_to_piece=promoted_to(piece.color, end)), position)
