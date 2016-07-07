
"""

rank
7 8 ║♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
6 7 ║♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
5 6 ║… … … … … … … …
4 5 ║… … … … … … … …
3 4 ║… … … … … … … …
2 3 ║… … … … … … … …
1 2 ║♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
0 1 ║♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
----╚═══════════════
——---a b c d e f g h
-----0 1 2 3 4 5 6 7
------file

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""
import copy

from core.algebraic.location import Location
from pieces.piece import Piece
from core.algebraic.move import Move
from core.algebraic import notation_const


class King(Piece):
    def __init__(self, input_color, location):
        super(King, self).__init__(input_color, location, "♚", "♔")

    def unfiltered(self, position):
        moves = []

        def add(function):
            if function(self.location).exit == 0:
                if position.is_square_empty(function(self.location)):
                    moves.append(Move(function(self.location), self, notation_const.MOVEMENT))

                elif not position.piece_at_square(function(self.location)).color.equals(self.color):
                    moves.append(Move(function(self.location), self, notation_const.CAPTURE))

        add(lambda x: x.shift_up())
        add(lambda x: x.shift_up_right())
        add(lambda x: x.shift_up_left())
        add(lambda x: x.shift_right())
        add(lambda x: x.shift_down())
        add(lambda x: x.shift_down_right())
        add(lambda x: x.shift_down_left())
        add(lambda x: x.shift_left())

        super(King, self).set_loc(moves)

        return moves

    def enemy_moves(self, position):
        moves = []

        # Loops through columns
        for row in position.position:

            # Loops through rows
            for piece in row:

                # Tests if square on the board is not empty
                if piece is not None and not piece.color.equals(self.color):

                    # Adds all of piece's possible moves to moves list.
                    moves.extend(piece.possible_moves(position))

        return moves

    def possible_moves(self, position):
        """

        :type position Board
        :return:
        """

        unfiltered = self.unfiltered(position)
        filtered = []

        for move in unfiltered:
            test = copy.deepcopy(position)
            test.update(move)
            legal = True
            for enemy_move in self.enemy_moves(test):
                # print("enemy Rank: ", enemy_move.rank, " File: ", enemy_move.file, " My Rank: ", self.location.rank, " File: ", self.location.file)
                # print("my shit ", end="")
                if enemy_move.end_location().equals(move.end_location()):
                    # print("happened", end="")
                    # move.print()
                    # enemy_move.print()
                    legal = False
                    break
            if legal:
                filtered.append(move)

        return filtered
