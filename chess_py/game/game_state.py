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
    return position.no_moves(color.white) \
        or position.no_moves(color.black)


def is_checkmate(position, input_color):
    """
    Finds if particular King is checkmated.

    :type: position: Board
    :type: input_color: Color
    :rtype: bool
    """
    return position.no_moves(input_color) and \
        position.get_king(input_color).in_check(position)
