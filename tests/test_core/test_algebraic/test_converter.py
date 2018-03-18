import unittest

from chess_py import converter, Board, Move, Location, color, notation_const
from chess_py import Pawn, Knight, Queen, Rook


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.test_board = Board.init_default()
        self.e_four_move = Move(end_loc=Location.from_string("e4"),
                                piece=Pawn(color.white, Location.from_string("e4")),
                                status=notation_const.MOVEMENT,
                                start_loc=Location.from_string("e2"))

    def test_short_alg(self):
        self.assertEqual(converter.short_alg("e4", color.white, self.test_board), self.e_four_move)

    def test_incomplete_alg_pawn_movement(self):
        self.assertEqual(
            converter.incomplete_alg("e4", color.white, self.test_board),
            Move(
                end_loc=Location.from_string("e4"),
                piece=Pawn(color.white, Location.from_string("e4")),
                status=notation_const.MOVEMENT,
                start_loc=Location.from_string("e2")
            )
        )

    def test_incomplete_alg_piece_movement(self):
        self.assertEqual(
            converter.incomplete_alg("Nf3", color.white, self.test_board),
            Move(
                end_loc=Location.from_string("f3"),
                piece=Knight(color.white, Location.from_string("f3")),
                status=notation_const.MOVEMENT,
                start_loc=Location.from_string("g1")
            )
        )

    def test_incomplete_alg_pawn_capture(self):
        self.test_board.update(converter.short_alg("e4", color.white, self.test_board))
        self.test_board.update(converter.short_alg("d5", color.black, self.test_board))
        self.assertEqual(
            converter.incomplete_alg("exd5", color.white, self.test_board),
            Move(
                end_loc=Location.from_string("d5"),
                piece=Pawn(color.white, Location.from_string("e4")),
                status=notation_const.CAPTURE,
                start_loc=Location.from_string("e4")
            )
        )

    def test_incomplete_alg_piece_capture(self):
        self.test_board.update(converter.short_alg("Nf3", color.white, self.test_board))
        self.test_board.update(converter.short_alg("e5", color.black, self.test_board))
        self.assertEqual(
            converter.incomplete_alg("Nxe5", color.white, self.test_board),
            Move(
                end_loc=Location.from_string("e5"),
                piece=Knight(color.white, Location.from_string("f3")),
                status=notation_const.CAPTURE,
                start_loc=Location.from_string("f3")
            )
        )

    def test_incomplete_alg_pawn_promotion(self):
        self.test_board.move_piece(Location.from_string("a2"), Location.from_string("a7"))
        self.test_board.remove_piece_at_square(Location.from_string("a8"))
        self.assertEqual(
            converter.incomplete_alg("a8=Q", color.white, self.test_board),
            Move(
                end_loc=Location.from_string("a8"),
                piece=Pawn(color.white, Location.from_string("e7")),
                status=notation_const.PROMOTE,
                promoted_to_piece=Queen,
                start_loc=Location.from_string("a7")
            )
        )

    def test_incomplete_alg_piece_movement_with_file_specified(self):
        self.assertEqual(
            converter.incomplete_alg("gNf3", color.white, self.test_board),
            Move(
                end_loc=Location.from_string("f3"),
                piece=Knight(color.white, Location.from_string("g1")),
                status=notation_const.MOVEMENT,
                start_loc=Location.from_string("g1")
            )
        )

    def test_incomplete_alg_piece_movement_with_file_specified_alt(self):
        self.assertEqual(
            converter.incomplete_alg("Ngf3", color.white, self.test_board),
            Move(
                end_loc=Location.from_string("f3"),
                piece=Knight(color.white, Location.from_string("g1")),
                status=notation_const.MOVEMENT,
                start_loc=Location.from_string("g1")
            )
        )

    def test_incomplete_alg_piece_movement_with_rank_and_file_specified(self):
        self.assertEqual(
            converter.incomplete_alg("e1Nf3", color.white, self.test_board),
            Move(
                end_loc=Location.from_string("f3"),
                piece=Knight(color.white, Location.from_string("e1")),
                status=notation_const.MOVEMENT,
                start_loc=Location.from_string("e1")
            )
        )

    def test_incomplete_alg_pawn_promotion_with_capture(self):
        self.test_board.move_piece(Location.from_string("a2"), Location.from_string("a7"))
        self.assertEqual(
            converter.incomplete_alg("axb8=R", color.white, self.test_board),
            Move(
                end_loc=Location.from_string("b8"),
                piece=Pawn(color.white, Location.from_string("a7")),
                status=notation_const.CAPTURE_AND_PROMOTE,
                promoted_to_piece=Rook,
                start_loc=Location.from_string("a7")
            )
        )
