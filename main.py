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

from setup.board import Board
from setup.algebraic.location import Location


def main():
    """
    Main method
    """
    print("New game creating")

    # Creates new game with human players for both white and black.
    """
    new_game = game.Game(human.Player(color.Color(color.white)), human.Player(color.Color(color.black)))
    new_game.start()
    """
    position = Board.init_default()
    position.print()

    position.move_piece(Location(1, 0), Location(2, 0))
    position.move_piece(Location(6, 1), Location(3, 1))
    position.print()

    print("Is the square empty", position.is_square_empty(Location(3, 0)))

    # print("This is the ghost symbol: " + position.piece_at_square(Location(3, 0)).symbol)

    for i in range(len(position.piece_at_square(Location(2, 0)).possible_moves(position))):
        position.piece_at_square(Location(2, 0)).possible_moves(position)[i].print()

    for j in range(len(position.piece_at_square(Location(3, 1)).possible_moves(position))):
        position.piece_at_square(Location(3, 1)).possible_moves(position)[j].print()


main()
