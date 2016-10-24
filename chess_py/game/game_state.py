# -*- coding: utf-8 -*-

"""
Static methods which check to see if
game is over, and if a King is checkmated.

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from ..core import color


def no_moves(position):
    """
    Finds if the game is over.

    :type: position: Board
    :rtype: bool
    """
    return len(position.all_possible_moves(color.white)) == 0 \
        or len(position.all_possible_moves(color.black)) == 0


def is_checkmate(position, input_color):
    """
    Finds if particular King is checkmated.

    :type: position: Board
    :type: input_color: Color
    :rtype: bool
    """
    return no_moves(position) and \
        position.piece_at_square(position.find_king(input_color)).in_check(position)
