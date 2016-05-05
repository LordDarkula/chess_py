class Bishop:
    def __init__(self, input_color):
        """
        Creates Bishop object that can be compared to and return possible moves
        :type input_color: color.Color
        """
        self.color = input_color.color
        # TODO add bishop move functionality

    def equals(self, piece):
        """
        Finds out if piece is the same type and color as self
        :type piece: pieces *
        """
        return type(piece) is type(self) and piece.white == self.white
