import unittest
from chess_py import converter, Board, Move, Location, Pawn, color, notation_const


class ConverterTest(unittest.TestCase):
    def setUp(self):
        self.test_board = Board.init_default()
        self.e_four_move = Move(Location(3, 4),
                                piece=Pawn(color.white, Location(1, 4)),
                                status=notation_const.MOVEMENT)

    def testShortAlg(self):
        self.assertEqual(converter.short_alg("e4", color.white, self.test_board), self.e_four_move)
