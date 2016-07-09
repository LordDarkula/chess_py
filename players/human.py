"""
Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from core import color, board



class Player:
    def __init__(self, input_color):
        """
        Creates interface for human player.
        :type input_color: color.Color
        """
        self.color = input_color

    def generate_move(self, position):
        """
        Returns valid and legal move given position
        :type position: board.Board
        """

        position.print()

        raw = str(input(self.color.string + "\'s move"))
        move = Converter(raw, self.color).get_move()

        while raw is not None and move.exit == 0:
            raw = str(input("Enter valid " + self.color.string + "\'s move"))
            move = Converter(raw, self.color).get_move()

        move = Converter(raw, self.color).get_move()

        return move
        # TODO eventually check move up against all_possible_moves


