from unittest import TestCase
from chess_py import color, Location, Move, Board, Knight


class TestKnight(TestCase):
    def setUp(self):
        self.empty_pos = Board([[None for _ in range(8)] for _ in range(8)])

    def test_possible_moves(self):
        self.empty_pos.place_piece_at_square(Knight(color.white, Location.from_string("e4")), Location.from_string("e4"))
        knight = self.empty_pos.piece_at_square(Location.from_string("e4"))

        moves = knight.possible_moves(self.empty_pos)
        self.assertEqual(len(list(moves)), 8)
