"""
Contains all classes that store and manipulate algebraic notation.
All algebraic inputs are converted and stored internally as . . .

rank and file - integers from 0 to 7
piece - child of Piece
color - Color

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

class Location:
    def __init__(self, rank, file):
        """
        Creates a location on a chessboard given x and y coordinates.
        :type rank: int
        :type file: int
        """
        self.rank = rank
        self.file = file
        self.exit = 0

        if not self.on_board():
            self.exit = 1

    def equals(self, location):
        """
        Finds is location on board is the same as current equation.
        :type location: algebraic.Location
        """
        return self.rank == location.rank and self.file == location.file

    def on_board(self):
        """
        Returns if the move is on the board or not.
        :rtype bool
        """
        if -1 < self.rank < 8 and -1 < self.file < 8:
            return True
        else:
            return False

    def shift_up(self):
        """
        Finds Location shifted up by 1
        :rtype: algebraic.Location
        """
        if self.rank < 7:
            self.exit = 0
            return Location(self.rank + 1, self.file)
        else:
            self.exit = 1
            return None

    def shift_down(self):
        """
        Finds Location shifted down by 1
        :rtype: algebraic.Location
        """
        if self.rank > 0:
            self.exit = 0
            return Location(self.rank - 1, self.file)
        else:
            self.exit = 1
            return None

    def shift_right(self):
        """
        Finds Location shifted right by 1
        :rtype: algebraic.Location
        """
        if self.file < 7:
            self.exit = 0
            return Location(self.rank, self.file + 1)

        else:
            self.exit = 1
            return None

    def shift_left(self):
        """
        Finds Location shifted left by 1
        :rtype: location.Location
        """
        if self.file > 0:
            self.exit = 0
            return Location(self.rank, self.file - 1)
        else:
            self.exit = 1
            return None

    def shift_up_right(self):
        """
        Finds Location shifted up right by 1
        :rtype: location.Location
        """
        if self.rank < 7 and self.file < 7:
            self.exit = 0
            return self.shift_up().shift_right()
        else:
            self.exit = 1
            return None

    def shift_up_left(self):
        """
        Finds Location shifted up left by 1
        :rtype: location.Location
        """
        if self.rank < 7 and self.file > 1:
            self.exit = 0
            return self.shift_up().shift_left()
        else:
            self.exit = 1
            return None

    def shift_down_right(self):
        """
        Finds Location shifted down right by 1
        :rtype: location.Location
        """
        if self.rank > 1 and self.file < 7:
            self.exit = 0
            return self.shift_up().shift_right()
        else:
            self.exit = 1
            return None

    def shift_down_left(self):
        """
        Finds Location shifted down left by 1
        :rtype: location.Location
        """
        if self.rank > 1 and self.file > 1:
            self.exit = 0
            return self.shift_up().shift_left()
        else:
            self.exit = 1
            return None