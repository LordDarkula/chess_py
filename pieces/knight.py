
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


from setup import color

class Knight:
    def __init__(self, input_color, location):
        """

        :type input_color: color.Color
        """
        self.color = input_color.color

        if self.color == color.white:
            self.symbol = "♞"
        else:
            self.symbol = "♘"
        # TODO add knight move functionality

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces *
        """
        return type(piece) is type(self) and piece.color == self.color

