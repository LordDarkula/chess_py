class King:
    def __init__(self, color):
        if color == "white":
            self.white = True

        self.white = False
        # TODO add knight king functionality

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces *
        """
        return type(piece) is type(self) and piece.white == self.white
