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
    except KeyError as e:
        raise ValueError("Piece {} is invalid".format(piece))


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

    if algebraic_string is None or len(algebraic_string) <= 1:
        raise ValueError("algebraic string {} is invalid".format(algebraic_string))

    # King side castle
    if algebraic_string in ["00", "oo", "OO", "0-0", "o-o", "O-O"]:
        return Move(Location(edge_rank(), 6),
                    piece=King(input_color, Location(edge_rank, 4)),
                    status=notation_const.KING_SIDE_CASTLE,
                    start_rank=edge_rank,
                    start_file=4)

    # Queen side castle
    if algebraic_string in ["000", "ooo", "OOO", "0-0-0", "o-o-o", "O-O-O"]:
        return Move(end_loc=Location(edge_rank(), 2),
                    piece=King(input_color, Location(edge_rank, 4)),
                    status=notation_const.QUEEN_SIDE_CASTLE,
                    start_rank=edge_rank,
                    start_file=4)

    # Pawn movement
    if len(algebraic_string) == 2:
        return Move(end_loc=Location(get_rank(1), get_file(0)),
                    piece=Pawn(input_color, end_loc),
                    status=notation_const.MOVEMENT)

    # Non-pawn Piece movement
    if len(algebraic_string) == 3:
        end_loc = Location(get_rank(2), get_file(1))
        try:
            return Move(end_loc=end_loc,
                        piece=_get_piece(algebraic_string, 0)(input_color, end_loc),
                        status=notation_const.MOVEMENT)
        except ValueError as error:
            raise ValueError(error)

    # multiple options
    if len(algebraic_string) == 4:

        # capture
        if algebraic_string[1].upper() == "X":

            # pawn capture
            if not algebraic_string[0].isupper():
                end_loc = Location(get_rank(3), get_file(2))
                return Move(end_loc=end_loc,
                            piece=Pawn(input_color, end_loc),
                            status=notation_const.CAPTURE,
                            start_file=get_file(0))

            # piece capture
            elif algebraic_string[0].isupper():
                end_loc = Location(get_rank(3), get_file(2))
                return Move(end_loc=end_loc,
                            piece=_get_piece(algebraic_string, 0)(input_color, end_loc),
                            status=notation_const.CAPTURE)

            # Pawn Promotion
            elif algebraic_string[2] == "=":
                end_loc = Location(get_rank(1), get_file(0))
                return Move(end_loc=end_loc,
                            piece=Pawn(input_color, end_loc),
                            status=notation_const.PROMOTE,
                            promoted_to_piece=_get_piece(algebraic_string, 3)(input_color, end_loc))

            # Non-pawn Piece movement with file specified
            elif algebraic_string[1].isupper():
                end_loc = Location(get_rank(3), get_file(2))
                return Move(end_loc=end_loc,
                            piece=_get_piece(algebraic_string, 1)(input_color, end_loc),
                            status=notation_const.MOVEMENT,
                            start_file=get_file(0))

            else:
                raise ValueError("algebraic string {} is invalid".format(algebraic_string))

    # Multiple options
    if len(algebraic_string) == 5:

        # Non-pawn Piece movement with rank and file specified
        if algebraic_string[2].isupper():
            return Move(end_loc=Location(get_rank(4), get_file(3)),
                        piece=_get_piece(algebraic_string, 2)(input_color, end_loc),
                        status=notation_const.MOVEMENT,
                        start_file=get_file(0),
                        start_rank=get_rank(1))

    # pawn promotion with capture
    if len(algebraic_string) == 6:

        # Pawn promote with capture
        return Move(end_loc=Location(get_rank(3), get_file(2)),
                    piece=Pawn(input_color, end_loc),
                    status=notation_const.MOVEMENT,
                    start_file=get_file(0),
                    promoted_to_piece=_get_piece(algebraic_string, 5)(input_color, end_loc))

    raise ValueError("algebraic string {} is invalid".format(algebraic_string))


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
