"""
Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""
import copy

from core.algebraic.location import Location
from core.algebraic.move import Move
from core.board import Board
from pieces.king import King


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


def legal_moves(position, color):
    """

    :type position Board
    :type color Color
    :return:
    """
    test = copy.deepcopy(position)
    king_loc = test.find_piece(King(color, Location(0, 0)))




def move(move, position):
    """

    :type move: Move
    :type position: Board
    """
    pass