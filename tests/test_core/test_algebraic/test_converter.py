import unittest

from chess_py import converter, Board, Move, Location, color, notation_const
from chess_py import Pawn, Knight, Queen, Rook


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.test_board = Board.init_default()
        self.e_four_move = Move(Location(3, 4),
                                piece=Pawn(color.white, Location(1, 4)),
                                status=notation_const.MOVEMENT)

    def test_short_alg(self):
        self.assertEqual(converter.short_alg("e4", color.white, self.test_board), self.e_four_move)

    def test_incomplete_alg_pawn_movement(self):
        self.assertEqual(
            converter.incomplete_alg("e4", color.white),
            Move(
                end_loc=Location.from_string("e4"),
                piece=Pawn(color.white, Location.from_string("e4")),
                status=notation_const.MOVEMENT
            )
        )

    def test_incomplete_alg_piece_movement(self):
        self.assertEqual(
            converter.incomplete_alg("Nb5", color.white),
            Move(
                end_loc=Location.from_string("b5"),
                piece=Knight(color.white, Location.from_string("b5")),
                status=notation_const.MOVEMENT
            )
        )

    def test_incomplete_alg_pawn_capture(self):
        self.assertEqual(
            converter.incomplete_alg("dxe5", color.black),
            Move(
                end_loc=Location.from_string("e5"),
                piece=Pawn(color.black, Location.from_string("e5")),
                status=notation_const.CAPTURE,
                start_file=3
            )
        )

    def test_incomplete_alg_piece_capture(self):
        self.assertEqual(
            converter.incomplete_alg("Nxa5", color.black),
            Move(
                end_loc=Location.from_string("a5"),
                piece=Knight(color.black, Location.from_string("a5")),
                status=notation_const.CAPTURE
            )
        )

    def test_incomplete_alg_pawn_promotion(self):
        self.assertEqual(
            converter.incomplete_alg("e8=Q", color.white),
            Move(
                end_loc=Location.from_string("e8"),
                piece=Pawn(color.white, Location.from_string("e8")),
                status=notation_const.PROMOTE,
                promoted_to_piece=Queen
            )
        )

    def test_incomplete_alg_piece_movement_with_file_specified(self):
        self.assertEqual(
            converter.incomplete_alg("aRb7", color.white),
            Move(
                end_loc=Location.from_string("b7"),
                piece=Rook(color.white, Location.from_string("b7")),
                status=notation_const.MOVEMENT,
                start_file=0
            )
        )

    def test_incomplete_alg_piece_movement_with_file_specified_alt(self):
        self.assertEqual(
            converter.incomplete_alg("Rab7", color.white),
            Move(
                end_loc=Location.from_string("b7"),
                piece=Rook(color.white, Location.from_string("b7")),
                status=notation_const.MOVEMENT,
                start_file=0
            )
        )

    def test_incomplete_alg_piece_movement_with_rank_and_file_specified(self):
        self.assertEqual(
            converter.incomplete_alg("a1Ra2", color.white),
            Move(
                end_loc=Location.from_string("a2"),
                piece=Rook(color.white, Location.from_string("a2")),
                status=notation_const.MOVEMENT,
                start_file=0,
                start_rank=0
            )
        )

    def test_incomplete_alg_pawn_promotion_with_capture(self):
        self.assertEqual(
            converter.incomplete_alg("exd8=R", color.white),
            Move(
                end_loc=Location.from_string("d8"),
                piece=Pawn(color.white, Location.from_string("d8")),
                status=notation_const.CAPTURE_AND_PROMOTE,
                promoted_to_piece=Rook
            )
        )
