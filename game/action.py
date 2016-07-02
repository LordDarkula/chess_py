"""
Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from core.algebraic.move import Move
from core.board import Board


def move_valid(position, move):
    """

    :type position: Board
    :type move: Move
    """
    if move.exit == 0:

        for k in range(len(position.all_possible_moves())):
            if move.equals(position.all_possible_moves()[k]):
                return True

    return False


def move(move, position):
    """

    :type move: Move
    :type position: Board
    """
    pass