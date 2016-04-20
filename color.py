
white = True
black = False

class Color:
    def __init__(self, color):
        """
        Initializes new color using bool with white = True and black = False
        :type color: bool
        """
        self.color = color
        if color:
            self.string = "white"
        else:
            self.string = "black"

    @classmethod
    def init_raw(cls, raw):
        cls.color = raw == "white"
        cls.string = raw

    def equals(self, color):
        """
        Finds out this color is the same as another color.
        :type color: Color
        """
        if type(color) is type(self):
            return self.color == color.color
        else:
            return self.color == color

