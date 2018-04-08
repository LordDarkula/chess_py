from unittest import TestCase
from chess_py import color, Location, Move, Board, King, converter, notation_const, Rook


class TestKing(TestCase):
    def setUp(self):
        self.board = Board.init_default()

    def test_in_check_as_result(self):
        self.assertFalse(self.board.get_king(color.white).in_check_as_result(self.board,
                                                 converter.long_alg("e2e4", self.board)))

        self.board.move_piece(Location.from_string("e1"), Location.from_string("e3"))
        self.board.move_piece(Location.from_string("e8"), Location.from_string("e5"))

        # self.assertTrue(self.board.get_king(color.white).in_check_as_result(self.board, converter.long_alg("e3e4", self.board)))

    def test_add(self):
        self.assertEqual(
            len(list(self.board.get_king(color.white).add(lambda  x: x.shift_up(), self.board))),
            0)

        self.board.update(converter.long_alg("e2e4", self.board))

        # King should be able to move up
        self.assertEqual(
            len(list(self.board.get_king(color.white).add(lambda x: x.shift_up(), self.board))),
            1)

        # King should not be able to move down
        self.assertEqual(
            len(list(self.board.get_king(color.white).add(lambda x: x.shift_down(), self.board))),
            0)

        # King should not be able to move left
        self.assertEqual(
            len(list(self.board.get_king(color.white).add(lambda x: x.shift_left(), self.board))),
            0)

        # King should not be able to move right
        self.assertEqual(
            len(list(self.board.get_king(color.white).add(lambda x: x.shift_right(), self.board))),
            0)

        # King should not be able to move up left
        self.assertEqual(
            len(list(self.board.get_king(color.white).add(lambda x: x.shift_up_left(), self.board))),
            0)

        # King should not be able to move down right
        self.assertEqual(
            len(list(self.board.get_king(color.white).add(lambda x: x.shift_down_right(), self.board))),
            0)

        # King should not be able to move down left
        self.assertEqual(
            len(list(self.board.get_king(color.white).add(lambda x: x.shift_down_left(), self.board))),
            0)

        # King should not be able to move up right
        self.assertEqual(
            len(list(self.board.get_king(color.white).add(lambda x: x.shift_up_right(), self.board))),
            0)

    def test_kingside_castle(self):
        self.board.update(converter.short_alg("e4", color.white, self.board))
        self.board.update(converter.short_alg("Nf3", color.white, self.board))
        self.board.update(converter.short_alg("Be2", color.white, self.board))

        castle_move = Move(
            end_loc=Location.from_string("g1"),
            piece=King(color.white, Location.from_string("g1")),
            status=notation_const.KING_SIDE_CASTLE,
            start_loc=Location.from_string("e1")
        )

        self.assertEqual(
            list(self.board.get_king(color.white).add_castle(self.board))[0], castle_move)

    def test_queenside_castle(self):

        self.board.remove_piece_at_square(Location.from_string("b1"))
        self.board.remove_piece_at_square(Location.from_string("c1"))
        self.board.remove_piece_at_square(Location.from_string("d1"))

        castle_move = Move(
            end_loc=Location.from_string("c1"),
            piece=King(color.white, Location.from_string("c1")),
            status=notation_const.QUEEN_SIDE_CASTLE,
            start_loc=Location.from_string("e1")
        )

        self.assertEqual(
            list(self.board.get_king(color.white).add_castle(self.board))[0], castle_move)

    def test_possible_moves(self):
        self.board = Board([[None for _ in range(8)] for _ in range(8)])
        my_king = King(color.white, Location.from_string("f3"))
        self.board.place_piece_at_square(my_king, Location.from_string("f3"))
        moves = ['f3f4', 'f3g3', 'f3f2', 'f3e3', 'f3g4', 'f3e4', 'f3g2', 'f3e2']

        for i, move in enumerate(my_king.possible_moves(self.board)):
            self.assertEqual(move, converter.long_alg(moves[i], self.board))

    def test_in_check(self):
        self.board = Board([[None for _ in range(8)] for _ in range(8)])
        my_king = King(color.white, Location.from_string("f3"))
        self.board.place_piece_at_square(my_king, Location.from_string("f3"))
        self.board.place_piece_at_square(Rook(color.black, Location.from_string("f1")), Location.from_string("f1"))

        print(self.board.piece_at_square(Location.from_string("f1")).color)

        print(self.board)
        print(my_king.color)
        print(color.white == color.black)
        self.assertTrue(my_king.in_check(self.board))

        self.board = Board.init_default()
        self.board.update(converter.long_alg("f2f3", self.board))
        self.board.move_piece(Location.from_string("d8"), Location.from_string("g3"))

        self.assertTrue(self.board.get_king(color.white).in_check(self.board))
