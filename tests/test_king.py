from unittest import TestCase
from chess_py import color, Location, Board, King, converter


class TestKing(TestCase):
    def setUp(self):
        self.board = Board.init_default()

    def test_in_check_as_result(self):
        self.assertFalse(King.in_check_as_result(self.board,
                                                 converter.long_alg("e2e4", self.board)))

        self.board.move_piece(Location.init_alg("d8"), Location.init_alg("f3"))


        self.assertTrue(King.in_check_as_result(self.board,
                                                 converter.long_alg("f3f2", self.board)))

    def test_add(self):
        self.assertEqual(
            len(self.board.get_king(color.white).add(lambda  x: x.shift_up(), self.board)),
            0)

        self.board.update(converter.long_alg("e2e4", self.board))

        # King should be able to move up
        self.assertEqual(
            len(self.board.get_king(color.white).add(lambda x: x.shift_up(), self.board)),
            1)

        # King should not be able to move down
        self.assertEqual(
            len(self.board.get_king(color.white).add(lambda x: x.shift_down(), self.board)),
            0)

        # King should not be able to move left
        self.assertEqual(
            len(self.board.get_king(color.white).add(lambda x: x.shift_left(), self.board)),
            0)

        # King should not be able to move right
        self.assertEqual(
            len(self.board.get_king(color.white).add(lambda x: x.shift_right(), self.board)),
            0)

        # King should not be able to move up left
        self.assertEqual(
            len(self.board.get_king(color.white).add(lambda x: x.shift_up_left(), self.board)),
            0)

        # King should not be able to move down right
        self.assertEqual(
            len(self.board.get_king(color.white).add(lambda x: x.shift_down_right(), self.board)),
            0)

        # King should not be able to move down left
        self.assertEqual(
            len(self.board.get_king(color.white).add(lambda x: x.shift_down_left(), self.board)),
            0)

        # King should not be able to move up right
        self.assertEqual(
            len(self.board.get_king(color.white).add(lambda x: x.shift_up_right(), self.board)),
            0)

    def test_add_castle(self):
        self.fail()

    def test_possible_moves(self):
        self.fail()

    def test_in_check(self):
        self.fail()
