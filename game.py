"""
Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from setup.board import Board


class Game:
    def __init__(self, player_white, player_black):
        """
        Creates new game given the players.
        :type player_white: human.Player or ai
        :type player_black: human.Player or ai
        """
        print("beginning of init")
        self.player_white = player_white
        self.player_black = player_black
        self.position = Board.init_default()
        print("init was called")

    def start(self):
        self.white_move()

    def white_move(self):
        move = self.player_white.generate_move(self.position)
        # TODO implement position change as a result of the move

    def black_move(self):
        move = self.player_black.generate_move(self.position)
        # TODO implement position change as a result of the move
