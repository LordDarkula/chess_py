"""
Chess playing program

8 ║♜♞♝♛♚♝♞♜
7 ║♟♟♟♟♟♟♟♟
6 ║……………………………………
5 ║……………………………………
4 ║……………………………………
3 ║……………………………………
2 ║♙♙♙♙♙♙♙♙
1 ║♖♘♗♕♔♗♘♖
--╚═══════════════
——-a b c d e f g h
"""

import game, human
from setup import color


def main():
    """
    Main method
    """
    print("New game creating")

    #Creates new game with human players for both white and black.
    new_game = game.Game(human.Player(color.Color(color.white)), human.Player(color.Color(color.black)))
    new_game.start()

main()
