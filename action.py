from setup import board
from setup.algebraic_notation import algebraic


def move_valid(position, move):
    """

    :type position: board.Board
    :type move: algebraic.Move
    """
    if move.not_none():

        for i in range(7):
            for j in range(7):

                if not position.is_square_empty(algebraic.Location(i, j)):

                    for p in range(position.piece_at_square(algebraic.Location(i, j)).possible_moves()):

                        if position.piece_at_square(algebraic.Location(i, j)).possible_moves()[p].equals(move):
                            return True

    return False

