# -*- coding: utf-8 -*-

"""
Class stores Knight on the board

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

from chess_py.core.algebraic import notation_const
from chess_py.pieces.piece import Piece

from chess_py.core.algebraic.move import Move


class Knight(Piece):
    def __init__(self, input_color, location):
        """
        Initializes Knight
        :type input_color: Color
        :type location Location
        """
        super(Knight, self).__init__(input_color, location, "♞", "♘")

    def possible_moves(self, position):
        """
        Finds all possible knight moves
        :type position Board
        :rtype: list
        """

        list_of_func = [lambda x: x.shift_up(), lambda x: x.shift_right(), lambda x: x.shift_down(),
                        lambda x: x.shift_left()]

        def cycle(index):
            """
            Cycles indexes containing shift directions perpendicular to current shift
            :type index int
            :rtype tuple
            """
            if index == 0:
                return index + 1, index + 3

            elif index == 3:
                return index - 1, index - 3

            return index + 1, index - 1

        def dest(loc, function, ind):
            """
            Returns both destinations that result when the knight is moved two steps in
            one of the cardinal directions
            :type loc Location
            :type function def
            :type ind int
            :rtype tuple
            """

            return list_of_func[cycle(ind)[0]](function(function(loc))), list_of_func[cycle(ind)[1]](function(
                function(loc)))

        moves = []

        for i in range(len(list_of_func)):
            dest_loc = dest(self.location, list_of_func[i], i)

            for j in range(2):
                if dest_loc[j].exit == 1:
                    status = notation_const.NOT_IMPLEMENTED
                elif position.is_square_empty(dest_loc[j]):
                    status = notation_const.MOVEMENT
                elif not position.piece_at_square(dest_loc[j]).color.equals(self.color):
                    status = notation_const.CAPTURE
                else:
                    status = notation_const.NOT_IMPLEMENTED

                if status != notation_const.NOT_IMPLEMENTED:
                    moves.append(Move(dest_loc[j], self, status))

        super(Knight, self).set_loc(moves)

        return moves
