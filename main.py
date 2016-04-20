"""
Chess playing program

8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
6 ║… … … … … … … …
5 ║… … … … … … … …
4 ║… … … … … … … …
3 ║… … … … … … … …
2 ║♙♙♙ ♙♙♙♙  ♙
1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
--╚═══════════════
——-a b c d e f g h
"""

import game
import human
from setup import color


def main():
    print("New game creating")
    new_game = game.Game(human.Player(color.Color(color.white)), human.Player(color.Color(color.black)))
