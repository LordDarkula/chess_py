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

    :raise: KeyError
    """
    piece = string[index].strip()
    piece = piece.upper()
    piece_dict = {'R': Rook,
                  'P': Pawn,
                  'B': Bishop,
                  'N': Knight,
                  'Q': Queen,
                  'K': King}
    try:
        return piece_dict[piece]
    except KeyError:
        raise ValueError("Piece {} is invalid".format(piece))


def incomplete_alg(alg_str, input_color):
    """
    Converts a string written in short algebraic form into an incomplete move.
    These incomplete moves do not have the initial location specified and
    therefore cannot be used to update the board. IN order to fully utilize
    incomplete move, it must be run through ``make_legal()`` with
    the corresponding position. It is recommended to use
    ``short_alg()`` instead of this method because it returns a complete
    move.

    Examples: e4, Nf3, exd5, Qxf3, 00, 000, e8=Q

    :type: alg_str: str
    :type: input_color: Color
    """
    def edge_rank():
        if input_color == color.white:
            return 0

        return 7

    if alg_str is None or len(alg_str) <= 1:
        raise ValueError("algebraic string {} is invalid".format(alg_str))

    # King side castle
    if alg_str in ["00", "oo", "OO", "0-0", "o-o", "O-O"]:
        return Move(Location(edge_rank(), 6),
                    piece=King(input_color, Location(edge_rank, 4)),
                    status=notation_const.KING_SIDE_CASTLE,
                    start_rank=edge_rank,
                    start_file=4)

    # Queen side castle
    if alg_str in ["000", "ooo", "OOO", "0-0-0", "o-o-o", "O-O-O"]:
        return Move(end_loc=Location(edge_rank(), 2),
                    piece=King(input_color, Location(edge_rank, 4)),
                    status=notation_const.QUEEN_SIDE_CASTLE,
                    start_rank=edge_rank,
                    start_file=4)

    end_location = Location.from_string(alg_str[-2:])

    # Pawn movement
    if len(alg_str) == 2:
        return Move(end_loc=end_location,
                    piece=Pawn(input_color, Location.from_string(alg_str)),
                    status=notation_const.MOVEMENT)

    # Non-pawn Piece movement
    if len(alg_str) == 3:
        try:
            return Move(end_loc=end_location,
                        piece=_get_piece(alg_str, 0)(input_color, end_location),
                        status=notation_const.MOVEMENT)
        except ValueError as error:
            raise ValueError(error)

    # multiple options
    if len(alg_str) == 4:

        # capture
        if alg_str[1].upper() == "X":

            # pawn capture
            if not alg_str[0].isupper():
                return Move(end_loc=end_location,
                            piece=Pawn(input_color, end_location),
                            status=notation_const.CAPTURE,
                            start_file=ord(alg_str[0]) - 97)

            # piece capture
            elif alg_str[0].isupper():
                return Move(end_loc=end_location,
                            piece=_get_piece(alg_str, 0)(input_color, end_location),
                            status=notation_const.CAPTURE)

            # Pawn Promotion
            elif alg_str[2] == "=":
                promote_end_loc = Location.from_string(alg_str[:2])
                return Move(end_loc=promote_end_loc,
                            piece=Pawn(input_color, promote_end_loc),
                            status=notation_const.PROMOTE,
                            promoted_to_piece=_get_piece(alg_str, 3)(input_color, promote_end_loc))

            # Non-pawn Piece movement with file specified
            elif alg_str[1].isupper():
                return Move(end_loc=end_location,
                            piece=_get_piece(alg_str, 1)(input_color, end_location),
                            status=notation_const.MOVEMENT,
                            start_file=ord(alg_str[0]) - 97)

            else:
                raise ValueError("algebraic string {} is invalid".format(alg_str))

    # Multiple options
    if len(alg_str) == 5:

        # Non-pawn Piece movement with rank and file specified
        if alg_str[2].isupper():
            start_loc = Location.from_string(alg_str[:2])
            return Move(end_loc=end_location,
                        piece=_get_piece(alg_str, 2)(input_color, end_location),
                        status=notation_const.MOVEMENT,
                        start_file=start_loc.file,
                        start_rank=start_loc.rank)

    # pawn promotion with capture
    if len(alg_str) == 6 and alg_str[4] == "=":
        promote_capture_end_loc = Location.from_string(alg_str[2:4])
        return Move(end_loc=promote_capture_end_loc,
                    piece=Pawn(input_color, promote_capture_end_loc),
                    status=notation_const.MOVEMENT,
                    start_file=ord(alg_str[0]) - 97,
                    promoted_to_piece=_get_piece(alg_str, 5)(input_color, promote_capture_end_loc))

    raise ValueError("algebraic string {} is invalid".format(alg_str))


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
    end = Location.from_string(alg_str[2:])
    start = Location.from_string(alg_str[:2])
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
