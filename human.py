
from setup import board, equality
from setup.algebraic_notation import algebraic


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
        for i in range(len(position.position)):
            for j in range(len(position.position[0])):
                print(position.position[i][j], end = "")
            print()

        move = str(input(self.color.string + "\'s move"))

        if equality.move_not_none(algebraic.Move(move, self.color)):
            return algebraic.Move(move, self.color)
        # TODO check if move is legal and if it isn't ask the user to enter a valid move

