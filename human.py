
from setup import board, algebraic, equality


class Player:
    def __init__(self, color):

        """
        Creates interface for human player.
        :type color: color.Color
        """
        self.color = color

    def generate_move(self, position):

        """
        Returns valid and legal move given position
        :type position: board.Board
        """
        for i in range(7):
            for j in range(7):
                print(position.position[i][j], end = "")

        move = str(input(self.color.string + "\'s move"))
        if equality.move_not_none(algebraic.Move(move, self.color)):
            return algebraic.Move(move, self.color)
        # TODO check if move is legal and if it isn't ask the user to enter a valid move

