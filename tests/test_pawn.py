from unittest import TestCase
from chess_py.pieces import Pawn
from chess_py.core import Board
from chess_py.core.algebraic.location import Location


class TestPawn(TestCase):
    def setUp(self):
        self.position = Board.init_default()
        self.white_pawn = self.position.piece_at_square(Location.init_alg("e2"))
        self.black_pawn = self.position.piece_at_square(Location.init_alg("a7"))

    def test_square_in_front(self):
        self.assertEqual(self.white_pawn.square_in_front(self.white_pawn.location), Location.init_alg("e3"))
        self.assertEqual(self.black_pawn.square_in_front(self.black_pawn.location), Location.init_alg("a6"))

    def test_two_squares_in_front(self):
        self.assertEqual(self.white_pawn.two_squares_in_front(self.white_pawn.location), Location.init_alg("e4"))
        self.assertEqual(self.black_pawn.two_squares_in_front(self.black_pawn.location), Location.init_alg("a5"))

    def test_would_move_be_promotion(self):
        self.assertTrue(self.white_pawn.would_move_be_promotion(Location.init_alg("e7")))
        self.assertTrue(self.black_pawn.would_move_be_promotion(Location.init_alg("a2")))
        self.assertFalse(self.white_pawn.would_move_be_promotion(Location.init_alg("e2")))
        self.assertFalse(self.black_pawn.would_move_be_promotion(Location.init_alg("a7")))

    def test_create_promotion_moves(self):
        self.fail()

    def test_forward_moves(self):
        self.fail()

    def test_capture_moves(self):
        self.fail()

    def test_en_passant_moves(self):
        self.fail()

    def test_possible_moves(self):
        self.fail()
