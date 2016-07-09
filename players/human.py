"""
Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from core import color, board
from core.algebraic import converter


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
        move = converter.to_move(raw, self.color)
        move = converter.make_legal(move, position)

        while raw is not None and move is not None:
            position.print()

            raw = str(input(self.color.string + "\'s move"))
            move = converter.to_move(raw, self.color)
            move = converter.make_legal(move, position)

        return move
