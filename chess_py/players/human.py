# -*- coding: utf-8 -*-

"""
Included class for human interaction via console.
Prints position and takes move written in algebraic notation as string input

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from pip._vendor.distlib.compat import raw_input
from chess_py.core.algebraic import converter
from chess_py.core.color import Color
from chess_py.players.player import Player
import sys


class Human(Player):
    def __init__(self, input_color):
        """
        Creates interface for human player.

        :type input_color: Color
        """
        super(Human, self).__init__(input_color)

    def generate_move(self, position):
        """
        Returns valid and legal move given position

        :type position: Board
        :rtype: Move
        """
        print(position)
        if sys.version_info[0] < 3:
            raw = raw_input(self.color.string + "\'s move \n")
        else:
            raw = input(self.color.string + "\'s move \n")
        move = None

        if len(raw) > 1:
            raw.strip()
            move = converter.short_alg(raw, self.color, position)

        while raw is None or move is None:

            if sys.version_info[0] < 3:
                raw = raw_input(self.color.string + "\'s move \n")
            else:
                raw = input(self.color.string + "\'s move \n")

            if len(raw) > 1:
                move = converter.short_alg(raw, self.color, position)

        return move
