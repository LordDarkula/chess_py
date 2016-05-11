
from setup import board
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
                    print(position.position[i][j].symbol + " ", end = "")
                else:
                    print("_ ", end = "")
            print()

        print()

        raw = str(input(self.color.string + "\'s move"))
        move = algebraic.Move(raw, self.color)

        while True:
            raw = str(input("Enter valid " + self.color.string + "\'s move"))
            if raw is not None and move.not_none():
                break

        move = algebraic.Move(raw, self.color)

        return move
        # TODO eventually check move up against all_possible_moves

