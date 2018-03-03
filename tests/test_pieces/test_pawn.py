from unittest import TestCase

from chess_py.core.algebraic import notation_const
from chess_py.core import Board
from chess_py.core.algebraic import Location, Move
from chess_py.pieces import Queen, Rook, Bishop, Knight, Pawn
from chess_py import color


class TestPawn(TestCase):
    def setUp(self):
        self.position = Board.init_default()

        self.white_pawn = Pawn(color.white, Location.from_string("e2"))
        self.position.place_piece_at_square(self.white_pawn, Location.from_string("e2"))

        self.black_pawn = Pawn(color.black, Location.from_string("a7"))
        self.position.place_piece_at_square(self.black_pawn, Location.from_string("a7"))

    def test_square_in_front(self):
        self.assertEqual(self.white_pawn.square_in_front(self.white_pawn.location), Location.from_string("e3"))
        self.assertEqual(self.black_pawn.square_in_front(self.black_pawn.location), Location.from_string("a6"))

    def test_two_squares_in_front(self):
        self.assertEqual(self.white_pawn.two_squares_in_front(self.white_pawn.location), Location.from_string("e4"))
        self.assertEqual(self.black_pawn.two_squares_in_front(self.black_pawn.location), Location.from_string("a5"))

    def test_would_move_be_promotion(self):
        self.assertTrue(self.white_pawn.would_move_be_promotion(Location.from_string("e7")))
        self.assertTrue(self.black_pawn.would_move_be_promotion(Location.from_string("a2")))
        self.assertFalse(self.white_pawn.would_move_be_promotion(Location.from_string("e2")))
        self.assertFalse(self.black_pawn.would_move_be_promotion(Location.from_string("a7")))

    def test_create_promotion_moves(self):
        self.white_pawn.location = Location.from_string("e7")
        moves = list(self.white_pawn.create_promotion_moves(notation_const.CAPTURE,
                                                            Location.from_string("e7")))
        self.assertEqual(len(list(moves)), 4)
        self.assertEqual(moves[0].start_loc, Location.from_string("e7"))

        self.assertEqual(moves[0].promoted_to_piece, Queen(color.white, Location.from_string("e8")))
        self.assertEqual(moves[1].promoted_to_piece, Rook(color.white, Location.from_string("e8")))
        self.assertEqual(moves[2].promoted_to_piece, Bishop(color.white, Location.from_string("e8")))
        self.assertEqual(moves[3].promoted_to_piece, Knight(color.white, Location.from_string("e8")))

    def test_forward_moves(self):
        self.white_pawn.location = Location.from_string("e2")
        moves = list(self.white_pawn.forward_moves(self.position))

        self.assertEqual(len(moves), 2)
        self.assertEqual(moves[0], Move(end_loc=self.white_pawn.square_in_front(self.white_pawn.location),
                                        piece=self.white_pawn,
                                        status=notation_const.MOVEMENT,
                                        start_rank=self.white_pawn.location.rank,
                                        start_file=self.white_pawn.location.file))

        self.assertEqual(moves[1], Move(end_loc=self.white_pawn.square_in_front(self.white_pawn.square_in_front(self.white_pawn.location)),
                                        piece=self.white_pawn,
                                        status=notation_const.MOVEMENT,
                                        start_rank=self.white_pawn.location.rank,
                                        start_file=self.white_pawn.location.file))

        moves = list(self.black_pawn.forward_moves(self.position))
        self.assertEqual(len(moves), 2)

        self.assertEqual(moves[0], Move(end_loc=self.black_pawn.square_in_front(self.black_pawn.location),
                                        piece=self.black_pawn,
                                        status=notation_const.MOVEMENT,
                                        start_rank=self.black_pawn.location.rank,
                                        start_file=self.black_pawn.location.file))

        self.assertEqual(moves[1], Move(end_loc=self.black_pawn.square_in_front(self.black_pawn.square_in_front(self.black_pawn.location)),
                                        piece=self.black_pawn,
                                        status=notation_const.MOVEMENT,
                                        start_rank=self.black_pawn.location.rank,
                                        start_file=self.black_pawn.location.file))

    def test_capture_moves(self):
        self.position.move_piece(Location.from_string("d7"), Location.from_string("d5"))
        self.position.move_piece(Location.from_string("e2"), Location.from_string("e4"))

        black_pawn = self.position.piece_at_square(Location.from_string("d5"))
        move = list(self.white_pawn.capture_moves(self.position))

        self.assertEqual(len(move), 1)

        self.assertEqual(move[0], Move(end_loc=black_pawn.location,
                                       piece=self.white_pawn,
                                       status=notation_const.CAPTURE,
                                       start_rank=self.white_pawn.location.rank,
                                       start_file=self.white_pawn.location.file))


    def test_en_passant_moves(self):
        self.position.move_piece(Location.from_string("d7"), Location.from_string("d4"))
        self.position.move_piece(Location.from_string("e2"), Location.from_string("e4"))

        black_pawn = self.position.piece_at_square(Location.from_string("d4"))
        self.position.piece_at_square(Location.from_string("e4")).just_moved_two_steps = True

        move = list(black_pawn.en_passant_moves(self.position))

        self.assertEqual(len(move), 1)
        self.assertEqual(move[0], Move(end_loc=black_pawn.square_in_front(black_pawn.location.shift_right()),
                                       piece=black_pawn,
                                       status=notation_const.EN_PASSANT,
                                       start_rank=black_pawn.location.rank,
                                       start_file=black_pawn.location.file))

    def test_possible_moves(self):
        self.assertEqual(len(list(self.white_pawn.possible_moves(self.position))), 2)
        self.position.move_piece(Location.from_string("e2"), Location.from_string("e3"))
        self.assertEqual(len(list(self.white_pawn.possible_moves(self.position))), 1)

