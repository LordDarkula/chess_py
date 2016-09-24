import unittest
from chess_py import short_alg, make_legal, Board, Move, Location, Pawn, color, notation_const


class ConverterTest(unittest.TestCase):

    def setUp(self):
        self.test_board = Board.init_default()
        self.e_four_move = Move(Location(3, 4),
                                piece=Pawn(color.Color.white(), Location(1, 4)),
                                status=notation_const.MOVEMENT)

    def testToMove(self):
        self.failUnless(short_alg("e4", color.Color.white()) == self.e_four_move)

if __name__ == '__main__':
    unittest.main()
