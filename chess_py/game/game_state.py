# -*- coding: utf-8 -*-

"""
Static methods which check to see if
game is over, and if a King is checkmated.

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""
from chess_py.core.color import Color


def no_moves(position):
    """
    Finds if the game is over.
    :type position Board
    :rtype bool
    """
    return len(position.all_possible_moves(Color.init_white())) == 0 \
        or len(position.all_possible_moves(Color.init_black())) == 0


def is_checkmate(position, color):
    """
    Finds if particular King is checkmated.
    :type position Board
    :type color Color
    :rtype bool
    """
    return no_moves(position) and \
        position.piece_at_square(position.find_king(color)).in_check(position)
