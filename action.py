from setup import board
from setup.algebraic_notation import algebraic


def move_valid(position, move):
    """

    :type position: board.Board
    :type move: algebraic.Move
    """
    if move.not_none():

        # Loops through columns
        for i in range(7):

            # Loops through rows
            for j in range(7):

                # Tests if square on the board is not empty and piece at that square is the same one specified in the move
                if not position.is_square_empty(algebraic.Location(i, j)) and position.piece_at_square(algebraic.Location(i, j)).equals(move.piece):

                    # Loops through list of possible moves that could be made by the piece on the square
                    for p in range(position.piece_at_square(algebraic.Location(i, j)).possible_moves()):

                        # Tests if the possible move matches given move
                        if position.piece_at_square(algebraic.Location(i, j)).possible_moves()[p].equals(move):
                            return True

    return False

