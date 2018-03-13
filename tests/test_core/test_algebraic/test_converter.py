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

    def test_incomplete_alg(self):
        self.assertEqual(
            converter.incomplete_alg("e4", color.white),
            Move(
                end_loc=Location.from_string("e4"),
                piece=Pawn(color.white, Location.from_string("e4")),
                status=notation_const.MOVEMENT
            )
        )

        self.assertEqual(
            converter.incomplete_alg("Nb5", color.white),
            Move(
                end_loc=Location.from_string("b5"),
                piece=Knight(color.white, Location.from_string("b5")),
                status=notation_const.MOVEMENT
            )
        )

        self.assertEqual(
            converter.incomplete_alg("dxe5", color.black),
            Move(
                end_loc=Location.from_string("e5"),
                piece=Pawn(color.black, Location.from_string("e5")),
                status=notation_const.CAPTURE,
                start_file=3
            )
        )

        self.assertEqual(
            converter.incomplete_alg("Nxa5", color.black),
            Move(
                end_loc=Location.from_string("a5"),
                piece=Knight(color.black, Location.from_string("a5")),
                status=notation_const.CAPTURE
            )
        )

        self.assertEqual(
            converter.incomplete_alg("e8=Q", color.white),
            Move(
                end_loc=Location.from_string("e8"),
                piece=Pawn(color.white, Location.from_string("e8")),
                status=notation_const.PROMOTE,
                promoted_to_piece=Queen(color.white, Location.from_string("e8"))
            )
        )

        self.assertEqual(
            converter.incomplete_alg("aRb7", color.white),
            Move(
                end_loc=Location.from_string("b7"),
                piece=Rook(color.white, Location.from_string("b7")),
                status=notation_const.MOVEMENT,
                start_file=0
            )
        )

        self.assertEqual(
            converter.incomplete_alg("Rab7", color.white),
            Move(
                end_loc=Location.from_string("b7"),
                piece=Rook(color.white, Location.from_string("b7")),
                status=notation_const.MOVEMENT,
                start_file=0
            )
        )

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

        self.assertEqual(
            converter.incomplete_alg("exd8=R", color.white),
            Move(
                end_loc=Location.from_string("d8"),
                piece=Pawn(color.white, Location.from_string("d8")),
                status=notation_const.CAPTURE_AND_PROMOTE,
                promoted_to_piece=Rook(color.white, Location.from_string("d8"))
            )
        )
