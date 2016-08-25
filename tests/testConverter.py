import unittest
from chess_py import to_move, make_legal, Board, Move, Location, Pawn, color, notation_const


class ConverterTest(unittest.TestCase):

    def setUp(self):
        self.test_board = Board.init_default()
        self.e_four_move = Move(Location(3, 4), Pawn(color.Color.init_white(), Location(1, 4)), notation_const.MOVEMENT)

    def testToMove(self):
        self.failUnless(to_move("e4", self.test_board).equals(self.e_four_move))

if __name__ == '__main__':
    unittest.main()
