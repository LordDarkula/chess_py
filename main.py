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

from chess_py import color, Human, Game


def main():
    """
    Main method
    """
    print("Creating a new game...")

    new_game = Game(Human(color.white), Human(color.black))
    result = new_game.play()

    print("Result is ", result)

if __name__ == "__main__":
    main()
