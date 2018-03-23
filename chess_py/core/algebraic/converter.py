# -*- coding: utf-8 -*-

"""
Methods that take external input and attempt
to turn them into usable commands.

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""
from copy import copy as cp

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


def _get_piece_start_location(end_location,
                              input_color,
                              piece_in_move,
                              position,
                              start_rank=None,
                              start_file=None):
    try:
        start_rank = int(start_rank) - 1
    except TypeError:
        pass
    try:
        start_file = ord(start_file) - 97
    except TypeError:
        pass

    def _is_at_start_rank_and_file(potential_start):
        if start_rank is not None and start_file is not None:
            return start_rank == potential_start.rank and \
                   start_file == potential_start.file
        elif start_rank is not None:
            return start_rank == potential_start.rank
        elif start_file is not None:
            return start_file == potential_start.file
        else:
            return True

    def _is_valid_move_option(move):
        real_piece = position.piece_at_square(move.end_loc)
        return type(real_piece) is piece_in_move and \
            real_piece.color == input_color and \
            _is_at_start_rank_and_file(move.end_loc)

    test_piece = piece_in_move(input_color, end_location)
    empty_board = Board([[None for _ in range(8)] for _ in range(8)])
    empty_board_valid_moves = [move for move in test_piece.possible_moves(empty_board)
                               if _is_valid_move_option(move)]

    if len(empty_board_valid_moves) == 1:
        return position.piece_at_square(empty_board_valid_moves[0].end_loc), \
               empty_board_valid_moves[0].end_loc
    else:
        for empty_board_move in empty_board_valid_moves:
            poss_piece = position.piece_at_square(empty_board_move.end_loc)
            for real_board_move in poss_piece.possible_moves(position):
                test_in_check_board = cp(position)
                test_move = Move(end_loc=real_board_move.end_loc,
                                 piece=test_in_check_board.piece_at_square(real_board_move.start_loc),
                                 status=real_board_move.status,
                                 start_loc=real_board_move.start_loc,
                                 promoted_to_piece=real_board_move.promoted_to_piece)
                test_in_check_board.update(test_move)
                if real_board_move.end_loc == end_location and \
                        not test_in_check_board.get_king(input_color).in_check(test_in_check_board):
                    return poss_piece, real_board_move.start_loc

    raise ValueError("No valid piece move found")


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
        possible_pawn = position.piece_at_square(end_location.shift_back(input_color))
        if type(possible_pawn) is Pawn and \
                possible_pawn.color == input_color:
            start_location = end_location.shift_back(input_color)
        else:
            start_location = end_location.shift_back(input_color, times=2)
        return Move(end_loc=end_location,
                    piece=position.piece_at_square(start_location),
                    status=notation_const.MOVEMENT,
                    start_loc=start_location)

    # Non-pawn Piece movement
    if len(alg_str) == 3:
        possible_piece, start_location = _get_piece_start_location(end_location,
                                                                   input_color,
                                                                   _get_piece(alg_str, 0),
                                                                   position)
        return Move(end_loc=end_location,
                    piece=possible_piece,
                    status=notation_const.MOVEMENT,
                    start_loc=start_location)

    # Multiple options (Capture or Piece movement with file specified)
    if len(alg_str) == 4:

        # Capture
        if alg_str[1].upper() == "X":

            # Pawn capture
            if not alg_str[0].isupper():
                pawn_location = Location(end_location.rank, ord(alg_str[0]) - 97).shift_back(input_color)
                possible_pawn = position.piece_at_square(pawn_location)
                if type(possible_pawn) is Pawn and \
                        possible_pawn.color == input_color:
                    en_passant_pawn = position.piece_at_square(end_location.shift_back(input_color))
                    if type(en_passant_pawn) is Pawn and \
                            en_passant_pawn.color != input_color and \
                            position.is_square_empty(end_location):
                        return Move(end_loc=end_location,
                                    piece=position.piece_at_square(pawn_location),
                                    status=notation_const.EN_PASSANT,
                                    start_loc=pawn_location)
                    else:
                        return Move(end_loc=end_location,
                                    piece=position.piece_at_square(pawn_location),
                                    status=notation_const.CAPTURE,
                                    start_loc=pawn_location)

            # Piece capture
            elif alg_str[0].isupper():
                possible_piece, start_location = _get_piece_start_location(end_location,
                                                                           input_color,
                                                                           _get_piece(alg_str, 0),
                                                                           position)
                return Move(end_loc=end_location,
                            piece=possible_piece,
                            status=notation_const.CAPTURE,
                            start_loc=start_location)

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
        elif alg_str[1].isupper() and not alg_str[0].isdigit():
            possible_piece, start_location = _get_piece_start_location(end_location,
                                                                       input_color,
                                                                       _get_piece(alg_str, 1),
                                                                       position,
                                                                       start_file=alg_str[0])
            return Move(end_loc=end_location,
                        piece=possible_piece,
                        status=notation_const.MOVEMENT,
                        start_loc=start_location)

        # (alt) Non-pawn Piece movement with file specified (Rab7)
        elif alg_str[0].isupper() and not alg_str[1].isdigit():
            possible_piece, start_location = _get_piece_start_location(end_location,
                                                                       input_color,
                                                                       _get_piece(alg_str, 0),
                                                                       position,
                                                                       start_file=alg_str[1])
            return Move(end_loc=end_location,
                        piece=possible_piece,
                        status=notation_const.MOVEMENT,
                        start_loc=start_location)

        # Non-pawn Piece movement with rank specified (R1b7)
        elif alg_str[0].isupper() and alg_str[1].isdigit():
            possible_piece, start_location = _get_piece_start_location(end_location,
                                                                       input_color,
                                                                       _get_piece(alg_str, 0),
                                                                       position,
                                                                       start_rank=alg_str[1])
            return Move(end_loc=end_location,
                        piece=possible_piece,
                        status=notation_const.MOVEMENT,
                        start_loc=start_location)

    # Multiple options
    if len(alg_str) == 5:

        # Non-pawn Piece movement with rank and file specified (a2Ra1
        if not alg_str[0].isdigit() and \
                alg_str[1].isdigit() and \
                alg_str[2].isupper() and \
                not alg_str[3].isdigit() and \
                alg_str[4].isdigit:
            start_loc = Location.from_string(alg_str[:2])
            return Move(end_loc=end_location,
                        piece=_get_piece(alg_str, 2)(input_color, end_location),
                        status=notation_const.MOVEMENT,
                        start_loc=start_loc)

        # Multiple Piece capture options
        if alg_str[2].upper() == "X":

            # Piece capture with rank specified (R1xa1)
            if alg_str[1].isdigit():
                possible_piece, start_location = _get_piece_start_location(end_location,
                                                                           input_color,
                                                                           _get_piece(alg_str, 0),
                                                                           position,
                                                                           start_rank=alg_str[1])
                return Move(end_loc=end_location,
                            piece=possible_piece,
                            status=notation_const.CAPTURE,
                            start_loc=start_location)

            # Piece capture with file specified (Rdxd7)
            else:
                possible_piece, start_location = _get_piece_start_location(end_location,
                                                                           input_color,
                                                                           _get_piece(alg_str, 0),
                                                                           position,
                                                                           start_file=alg_str[1])
                return Move(end_loc=end_location,
                            piece=possible_piece,
                            status=notation_const.CAPTURE,
                            start_loc=start_location)

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

    raise ValueError("Move {} not legal in \n{}".format(repr(move), position))


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
            promoted_to is King or \
            promoted_to is Pawn:
        raise Exception("Invalid move input")

    return make_legal(Move(end_loc=end,
                           piece=piece,
                           status=notation_const.LONG_ALG,
                           start_loc=start,
                           promoted_to_piece=promoted_to), position)
