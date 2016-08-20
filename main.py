# -*- coding: utf-8 -*-

"""
Chess playing program
Everything starts here


8 ║♜♞♝♛♚♝♞♜
7 ║♟♟♟♟♟♟♟♟
6 ║…………………………………
5 ║…………………………………
4 ║…………………………………
3 ║…………………………………
2 ║♙♙♙♙♙♙♙♙
1 ║♖♘♗♕♔♗♘♖
--╚═══════════════
——-a b c d e f g h

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from chess_py import Color, Player, Game
from chess_py.players.basicAI import Ai


def main():
    """
    Main method
    """
    print("Creating a new game...")

    # Creates new game with human players for both white and black.

    new_game = Game(Player(Color.init_white()), Player(Color.init_black()))
    result = new_game.play()

    print("Result is ", result)

    # position.piece_at_square(Location(4, 1)).just_moved_two_steps = True

    # out("This is the ghost symbol: " + position.piece_at_square(Location(3, 0)).symbol)

    # for i in range(len(position.all_possible_moves(Color(True)))):
    #    position.all_possible_moves(Color(True))[i].out()

if __name__ == "__main__":
    main()
