
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
                if position.position[i][j] is not None:
                    print(position.position[i][j].symbol, end = "")
                else:
                    print("_", end = "")
            print()

        print()

        raw = str(input(self.color.string + "\'s move"))

        move = algebraic.Move(raw, self.color)
        while raw is None or move.not_none():
            raw = str("Enter valid " + input(self.color.string + "\'s move"))

        return move
        # TODO check if move is legal and if it isn't ask the user to enter a valid move

