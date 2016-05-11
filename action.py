from setup import board
from setup.algebraic_notation import algebraic


def move_valid(position, move):
    """

    :type position: board.Board
    :type move: algebraic.Move
    """
    if move.not_none():

        for k in range(len(position.all_possible_moves())):
            if move.equals(position.all_possible_moves()[k]):
                return True

    return False