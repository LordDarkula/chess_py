class Queen:
    def __init__(self, color):
        if color == "white":
            self.white = True

        self.white = False
        # TODO add queen move functionality

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces *
        """
        return type(piece) is type(self) and piece.white == self.white
