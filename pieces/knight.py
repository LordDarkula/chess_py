#TODO debug this voodoo thoroughly
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


from setup.color import Color
from pieces.piece import Piece
from setup.algebraic_notation.algebraic import Location, Move
from setup.algebraic_notation import notation_const
from setup.board import Board

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

        list_of_func = [lambda x:x.shift_up(), lambda x:x.shift_right(), lambda x:x.shift_down(), lambda x:x.shift_left()]
        twice = lambda loc, function: loc.function().function()

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

            :type loc Location
            :type function def
            :type ind int
            :rtype tuple
            """
            return twice(loc, function).list_of_func[cycle(ind)[0]], twice(loc, function).list_of_func[cycle(ind)[1]]
        moves = []

        for i in range(len(list_of_func)):
            dest_loc = dest(self.location, list_of_func[i], i)
            for j in range(1):
                if position.is_square_empty(dest_loc[j]):
                    status = notation_const.MOVEMENT
                elif not position.piece_at_square(dest_loc[j]).color.equals(self.color):
                    status = notation_const.CAPTURE
                else:
                    status = notation_const.NOT_IMPLEMENTED

                if status != notation_const.NOT_IMPLEMENTED:
                    moves.append(Move.init_loc(dest_loc[j], self, status))
        return moves