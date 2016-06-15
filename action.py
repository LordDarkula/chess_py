"""
Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from setup import board
from setup.algebraic_notation import algebraic


def move_valid(position, move):
    """

    :type position: board.Board
    :type move: algebraic.Move
    """
    if move.exit == 0:

        for k in range(len(position.all_possible_moves())):
            if move.equals(position.all_possible_moves()[k]):
                return True

    return False

def move(move, position):
    """

    :type move: algebrqic.Move
    :type position: board.Board
    """
    pass