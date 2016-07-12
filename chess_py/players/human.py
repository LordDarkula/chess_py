# -*- coding: utf-8 -*-

"""
Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from chess_py.core.algebraic import converter

from chess_py.core import color


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

        raw = str(input(self.color.string + "\'s move \n"))
        raw.strip()
        move = converter.to_move(raw, self.color)
        move = converter.make_legal(move, position)

        while raw is None or move is None:

            raw = str(input("Enter valid " + self.color.string + "\'s move \n"))
            raw.strip()
            move = converter.to_move(raw, self.color)
            move = converter.make_legal(move, position)

        return move
