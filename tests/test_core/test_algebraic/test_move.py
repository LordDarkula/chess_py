import unittest
import copy

from chess_py import Move, Location, notation_const, Pawn, color, Queen


class TestMove(unittest.TestCase):

    def setUp(self):
        self.white_pawn = Pawn(color.white, Location(1, 0))
        self.black_pawn = Pawn(color.black, Location(1, 0))

        self.white_pawn_move = Move(Location(2, 0),
                                    piece=self.white_pawn,
                                    status=notation_const.MOVEMENT)

        self.start_specified = Move(Location(2, 0),
                                    piece=self.white_pawn,
                                    status=notation_const.MOVEMENT,
                                    start_rank=3,
                                    start_file=5)

    def testStr(self):
        self.assertEquals(str(self.start_specified), "f4a3")

        self.white_pawn_move = Move(Location(7, 0),
                                    piece=self.white_pawn,
                                    status=notation_const.MOVEMENT,
                                    start_rank=6,
                                    start_file=0,
                                    promoted_to_piece=Queen(color.white,
                                                            Location(7, 0)))

    def testEquals(self):
        print(self.white_pawn_move.status == notation_const.MOVEMENT)

        test_copy = copy.copy(self.white_pawn_move)
        print(self.white_pawn_move == test_copy)
        self.assertEqual(self.white_pawn_move, Move(end_loc=Location(2, 0),
                                                    piece=self.white_pawn,
                                                    status=notation_const.MOVEMENT))

        self.assertEqual(self.white_pawn_move, Move(end_loc=Location(2, 0),
                                                    piece=self.white_pawn,
                                                    status=notation_const.MOVEMENT,
                                                    start_rank=1,
                                                    start_file=0))


if __name__ == '__main__':
    unittest.main()
