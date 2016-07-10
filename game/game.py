"""
Class that holds state of a game.
Start game using play(), which returns the result
when the game is finished.

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from core.board import Board
from core.color import Color
from game.game_state import *
from core.algebraic.converter import *
import itertools


class Game:
    def __init__(self, player_white, player_black):
        """
        Creates new game given the players.
        :type player_white: human.Player or ai
        :type player_black: human.Player or ai
        """
        self.player_white = player_white
        self.player_black = player_black
        self.position = Board.init_default()

    def play(self):
        """
        Starts game and returns one of 3 results . .

        1 - White wins
        0.5 - Draw
        0 - Black wins

        :rtype int
        """
        print("starting play")
        colors = [lambda: self.white_move(), lambda: self.black_move()]
        colors = itertools.cycle(colors)

        while True:
            print("Entered play loop")
            self.position.print()
            color_fn = next(colors)
            if no_moves(self.position):
                print("No moves")
                if self.position.get_king(Color.init_black()).in_check(self.position):
                    return 1

                elif self.position.get_king(Color.init_white()).in_check(self.position):
                    return 0
                else:
                    return 0.5

            self.position.print()
            print("Called color_fn")
            color_fn()

    def white_move(self):
        move = self.player_white.generate_move(self.position)
        move = make_legal(move, self.position)
        self.position.update(move)
        self.position.print()

    def black_move(self):
        move = self.player_black.generate_move(self.position)
        move = make_legal(move, self.position)
        self.position.update(move)
        self.position.print()

    def all_possible_moves(self, input_color):
        return self.position.all_possible_moves(input_color)