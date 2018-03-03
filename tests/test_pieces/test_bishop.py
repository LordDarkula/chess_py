from unittest import TestCase

from chess_py import Board, Location, converter


class TestBishop(TestCase):
    def setUp(self):
        self.board = Board.init_default()

    def test_no_possible_moves(self):
        self.assertEqual(len(list(self.board.piece_at_square(Location.from_string("c1"))
                             .possible_moves(self.board))), 0)

    def test_left_diagonal(self):
        self.board.update(converter.long_alg("b2b3", self.board))
        moves = list(self.board.piece_at_square(Location.from_string("c1")).possible_moves(self.board))

        self.assertEqual(len(moves), 2)
        self.assertEqual(moves[0], converter.long_alg("c1b2", self.board))
        self.assertEqual(moves[1], converter.long_alg("c1a3", self.board))

    def test_capture(self):
        self.board.move_piece(Location.from_string("g1"), Location.from_string("g7"))
        moves = list(self.board.piece_at_square(Location.from_string("f8")).possible_moves(self.board))

        self.assertEqual(len(moves), 1)
        self.assertEqual(moves[0], converter.long_alg("f8g7", self.board))

    def test_possible_moves(self):
        self.board.move_piece(Location.from_string("c1"), Location.from_string("d4"))
        test_moves = self.board.piece_at_square(Location.from_string("d4")).possible_moves(self.board)
        real_moves = ["d4e5", "d4f6", "d4g7", "d4c5", "d4b6", "d4a7", "d4e3", "d4c3"]

        for i, move in enumerate(test_moves):
            self.assertEqual(str(move), real_moves[i])


