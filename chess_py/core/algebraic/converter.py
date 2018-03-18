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
from ..board import Board
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


def incomplete_alg(alg_str, input_color, position):
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
    edge_rank = 0 \
        if input_color == color.white \
        else 7

    if alg_str is None or len(alg_str) <= 1:
        raise ValueError("algebraic string {} is invalid".format(alg_str))

    # King-side castle
    if alg_str in ["00", "oo", "OO", "0-0", "o-o", "O-O"]:
        return Move(end_loc=Location(edge_rank, 6),
                    piece=King(input_color, Location(edge_rank, 4)),
                    status=notation_const.KING_SIDE_CASTLE,
                    start_loc=Location(edge_rank, 4))

    # Queen-side castle
    if alg_str in ["000", "ooo", "OOO", "0-0-0", "o-o-o", "O-O-O"]:
        return Move(end_loc=Location(edge_rank, 2),
                    piece=King(input_color, Location(edge_rank, 4)),
                    status=notation_const.QUEEN_SIDE_CASTLE,
                    start_loc=Location(edge_rank, 4))
    try:
        end_location = Location.from_string(alg_str[-2:])
    except ValueError:
        end_location = Location.from_string(alg_str[-4:-2])

    # Pawn movement
    if len(alg_str) == 2:
        if type(position.piece_at_square(end_location.shift_back(input_color))) == Pawn and \
                position.piece_at_square(end_location.shift_back(input_color)).color == input_color:
            start_location = end_location.shift_back(input_color)
        else:
            start_location = end_location.shift_back(input_color, times=2)
        return Move(end_loc=end_location,
                    piece=position.piece_at_square(start_location),
                    status=notation_const.MOVEMENT,
                    start_loc=start_location)

    # Non-pawn Piece movement
    if len(alg_str) == 3:
        try:
            test_piece = _get_piece(alg_str, 0)(input_color, end_location)
            empty_board = Board([[None for _ in range(8)] for _ in range(8)])
            for move in test_piece.possible_moves(empty_board):
                if type(position.piece_at_square(move.end_loc)) is _get_piece(alg_str, 0):
                    return Move(end_loc=end_location,
                                piece=position.piece_at_square(move.end_loc),
                                status=notation_const.MOVEMENT,
                                start_loc=move.end_loc)
        except ValueError as error:
            raise ValueError(error)

    # Multiple options (Capture or Piece movement with file specified)
    if len(alg_str) == 4:

        # Capture
        if alg_str[1].upper() == "X":

            # Pawn capture
            if not alg_str[0].isupper():
                start_file = ord(alg_str[0]) - 97
                return Move(end_loc=end_location,
                            piece=Pawn(input_color, end_location),
                            status=notation_const.CAPTURE,
                            start_loc=Location(end_location.rank, start_file).shift_back(input_color))

            # Piece capture
            elif alg_str[0].isupper():
                try:
                    test_piece = _get_piece(alg_str, 0)(input_color, end_location)
                    empty_board = Board([[None for _ in range(8)] for _ in range(8)])
                    for move in test_piece.possible_moves(empty_board):
                        if type(position.piece_at_square(move.end_loc)) is _get_piece(alg_str, 0):
                            return Move(end_loc=end_location,
                                        piece=position.piece_at_square(move.end_loc),
                                        status=notation_const.CAPTURE,
                                        start_loc=move.end_loc)
                except ValueError as error:
                    raise ValueError(error)

        # Pawn Promotion
        elif alg_str[2] == "=":
            promote_end_loc = Location.from_string(alg_str[:2])
            if promote_end_loc.rank != 0 and promote_end_loc.rank != 7:
                raise ValueError("Promotion {} must be on the last rank".format(alg_str))
            return Move(end_loc=promote_end_loc,
                        piece=Pawn(input_color, promote_end_loc),
                        status=notation_const.PROMOTE,
                        promoted_to_piece=_get_piece(alg_str, 3),
                        start_loc=promote_end_loc.shift_back(input_color))

        # Non-pawn Piece movement with file specified (aRb7)
        elif alg_str[1].isupper():
            try:
                test_piece = _get_piece(alg_str, 1)(input_color, end_location)
                empty_board = Board([[None for _ in range(8)] for _ in range(8)])
                start_file = ord(alg_str[0]) - 97
                for move in test_piece.possible_moves(empty_board):
                    if type(position.piece_at_square(move.end_loc)) is _get_piece(alg_str, 1) and \
                            move.end_loc.file == start_file:
                        return Move(end_loc=end_location,
                                    piece=position.piece_at_square(move.end_loc),
                                    status=notation_const.MOVEMENT,
                                    start_loc=move.end_loc)
            except ValueError as error:
                raise ValueError(error)

        # (alt) Non-pawn Piece movement with file specified (Rab7)
        elif alg_str[0].isupper():
            try:
                test_piece = _get_piece(alg_str, 0)(input_color, end_location)
                start_file = ord(alg_str[1]) - 97
                empty_board = Board([[None for _ in range(8)] for _ in range(8)])
                for move in test_piece.possible_moves(empty_board):
                    if type(position.piece_at_square(move.end_loc)) is _get_piece(alg_str, 0) and \
                            move.end_loc.file == start_file:
                        return Move(end_loc=end_location,
                                    piece=position.piece_at_square(move.end_loc),
                                    status=notation_const.MOVEMENT,
                                    start_loc=move.end_loc)
            except ValueError as error:
                raise ValueError(error)

    # Multiple options
    if len(alg_str) == 5:

        # Non-pawn Piece movement with rank and file specified
        if alg_str[2].isupper():
            start_loc = Location.from_string(alg_str[:2])
            return Move(end_loc=end_location,
                        piece=_get_piece(alg_str, 2)(input_color, end_location),
                        status=notation_const.MOVEMENT,
                        start_loc=start_loc)

    # Pawn promotion with capture
    if len(alg_str) == 6 and alg_str[4] == "=":
        start_file = ord(alg_str[0]) - 97
        promote_capture_end_loc = Location.from_string(alg_str[2:4])
        return Move(end_loc=promote_capture_end_loc,
                    piece=Pawn(input_color, promote_capture_end_loc),
                    status=notation_const.CAPTURE_AND_PROMOTE,
                    promoted_to_piece=_get_piece(alg_str, 5),
                    start_loc=Location(end_location.shift_back(input_color).rank, start_file))

    raise ValueError("algebraic string {} is invalid in \n{}".format(alg_str, position))


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
    for legal_move in position.all_possible_moves(move.color):

        if move.status == notation_const.LONG_ALG:
            if move.end_loc == legal_move.end_loc and \
                    move.start_loc == legal_move.start_loc:
                return legal_move

        elif move == legal_move:
            return legal_move

    raise ValueError("Move {} not legal in \n{}".format(move, position))


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
    return make_legal(incomplete_alg(algebraic_string, input_color, position), position)


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
    if alg_str is None or len(alg_str) < 4 or len(alg_str) > 6:
        raise ValueError("Invalid string input {}".format(alg_str))

    end = Location.from_string(alg_str[2:])
    start = Location.from_string(alg_str[:2])
    piece = position.piece_at_square(start)

    if len(alg_str) == 4:
        return make_legal(Move(end_loc=end,
                               piece=piece,
                               status=notation_const.LONG_ALG,
                               start_loc=start), position)

    promoted_to = _get_piece(alg_str, 4)
    if promoted_to is None or \
            isinstance(promoted_to, King) or \
            isinstance(promoted_to, Pawn):
        raise Exception("Invalid move input")

    return make_legal(Move(end_loc=end,
                           piece=piece,
                           status=notation_const.LONG_ALG,
                           start_loc=start,
                           promoted_to_piece=promoted_to(piece.color, end)), position)
