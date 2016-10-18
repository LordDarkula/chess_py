from unittest import TestCase
from chess_py import Location, Board, King, converter


class TestKing(TestCase):
    def setUp(self):
        self.board = Board.init_default()

    def test_in_check_as_result(self):
        self.assertFalse(King.in_check_as_result(self.board,
                                                 converter.long_alg("e2e4", self.board)))

        self.board.move_piece(Location.init_alg("d8"), Location.init_alg("f3"))

        print(self.board)

        self.assertTrue(King.in_check_as_result(self.board,
                                                 converter.long_alg("f3f2", self.board)))
        print(self.board)

    def test_add(self):
        self.fail()

    def test_add_castle(self):
        self.fail()

    def test_possible_moves(self):
        self.fail()

    def test_in_check(self):
        self.fail()
