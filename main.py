"""
Chess playing program
Everything starts here


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

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from setup.board import Board
from setup.algebraic_notation.location import Location


def main():
    """
    Main method
    """
    print("New game creating")

    #Creates new game with human players for both white and black.
    """
    new_game = game.Game(human.Player(color.Color(color.white)), human.Player(color.Color(color.black)))
    new_game.start()
    """
    position = Board.init_default()
    position.print()
    position.move_piece(Location(0,0), Location(0,1))
    position.print()

main()