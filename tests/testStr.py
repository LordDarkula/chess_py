import unittest
from chess_py import Move, Location, Pawn, color, notation_const, Queen


class StrTest(unittest.TestCase):

    def setUp(self):
        self.white_pawn = Pawn(color.Color.init_white(), Location(1, 0))
        self.white_pawn_move = Move(Location(2, 0),
                                    piece=self.white_pawn,
                                    status=notation_const.MOVEMENT,
                                    start_rank=1,
                                    start_file=0)

    def testLocationStr(self):
        self.assertEquals(str(Location(3, 4)), "e4")
        self.assertEquals(str(Location(0, 0)), "a1")
        self.assertEquals(str(Location(7, 7)), "h8")

    def testMoveStr(self):
        self.assertEquals(str(self.white_pawn_move), "a2a3")

        self.white_pawn_move = Move(Location(7, 0),
                                    piece=self.white_pawn,
                                    status=notation_const.MOVEMENT,
                                    start_rank=6,
                                    start_file=0,
                                    promoted_to_piece=Queen(color.Color.init_white(),
                                                            Location(7, 0)))

        self.assertEquals(str(self.white_pawn_move), "a7a8Q")
