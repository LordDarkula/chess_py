import unittest

from chess_py import Move, Location, notation_const, Pawn, color


class MoveTest(unittest.TestCase):

    def setUp(self):
        self.white_pawn = Pawn(color.Color.init_white(), Location(1, 0))
        self.black_pawn = Pawn(color.Color.init_black(), Location(1, 0))
        self.white_pawn_move = Move(Location(2, 0),
                                    piece=self.white_pawn,
                                    status=notation_const.MOVEMENT)

        self.start_specified = Move(Location(2, 0),
                                    piece=self.white_pawn,
                                    status=notation_const.MOVEMENT,
                                    start_rank=3,
                                    start_file=5)

    def testEquals(self):
        self.failUnless(self.white_pawn_move.equals(Move(end_loc=Location(2, 0),
                                                         piece=self.white_pawn,
                                                         status=notation_const.MOVEMENT)))

        self.failUnless(self.white_pawn_move.equals(Move(end_loc=Location(2, 0),
                                                         piece=self.white_pawn,
                                                         status=notation_const.MOVEMENT,
                                                         start_rank=1,
                                                         start_file=0)))

        self.failIf(self.white_pawn_move.equals(Move(end_loc=Location(1, 0),
                                                     piece=self.white_pawn,
                                                     status=notation_const.MOVEMENT)))

        self.failIf(self.white_pawn_move.equals(Move(end_loc=Location(2, 0),
                                                     piece=self.black_pawn,
                                                     status=notation_const.MOVEMENT)))

        self.failIf(self.white_pawn_move.equals(Move(end_loc=Location(2, 0),
                                                     piece=self.white_pawn,
                                                     status=notation_const.CAPTURE)))

        self.failIf(self.start_specified.equals(Move(end_loc=Location(2, 0),
                                                     piece=self.white_pawn,
                                                     status=notation_const.MOVEMENT,
                                                     start_rank=1,
                                                     start_file=0)))

    def testOnBoard(self):
        self.failUnless(self.white_pawn_move.on_board())
        self.failIf(Move(Location(8, 4), self.white_pawn, notation_const.MOVEMENT).on_board())

if __name__ == '__main__':
    unittest.main()
