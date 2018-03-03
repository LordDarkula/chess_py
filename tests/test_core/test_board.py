from unittest import TestCase

from chess_py import Board, color, Location
from chess_py import Pawn, Knight, Bishop, Rook, Queen, King, piece_const, converter


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board.init_default()

    def test_init_default(self):
        white = color.white
        black = color.black
        test = Board([

        # First rank
        [Rook(white, Location(0, 0)), Knight(white, Location(0, 1)), Bishop(white, Location(0, 2)),
         Queen(white, Location(0, 3)), King(white, Location(0, 4)), Bishop(white, Location(0, 5)),
         Knight(white, Location(0, 6)), Rook(white, Location(0, 7))],

        # Second rank
        [Pawn(white, Location(1, file)) for file in range(8)],


        # Third rank
        [None for _ in range(8)],

        # Fourth rank
        [None for _ in range(8)],

        # Fifth rank
        [None for _ in range(8)],

        # Sixth rank
        [None for _ in range(8)],

        # Seventh rank
        [Pawn(black, Location(6, file)) for file in range(8)],

        # Eighth rank
        [Rook(black, Location(7, 0)), Knight(black, Location(7, 1)), Bishop(black, Location(7, 2)),
         Queen(black, Location(7, 3)), King(black, Location(7, 4)), Bishop(black, Location(7, 5)),
         Knight(black, Location(7, 6)), Rook(black, Location(7, 7))]])

        self.assertEqual(self.board, test)

    def test_copy(self):
        tester = Board.init_default()

        for num, row in enumerate(self.board.position):
            for index, piece in enumerate(row):
                self.assertEqual(piece, tester.position[num][index])

    def test_piece_at_square(self):
        self.assertEqual(self.board.piece_at_square(Location(0, 0)),
                          Rook(color.white, Location(0, 0)))

        self.assertEqual(self.board.piece_at_square(Location(1, 0)),
                          Pawn(color.white, Location(1, 0)))

        self.assertEqual(self.board.piece_at_square(Location(0, 1)),
                          Knight(color.white, Location(0, 1)))

    def test_is_square_empty(self):
        self.assertTrue(self.board.is_square_empty(Location(2, 0)))
        self.assertFalse(self.board.is_square_empty(Location(0, 3)))

    def test_material_advantage(self):
        self.assertEqual(self.board.material_advantage(color.white, piece_const.PieceValues()), 0)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.PieceValues()), 0)

        self.board.position[0][0] = None

        self.assertEqual(self.board.material_advantage(color.white, piece_const.PieceValues()), -5)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.PieceValues()), 5)

        self.board = Board.init_default()
        self.board.position[0][1] = None

        self.assertEqual(self.board.material_advantage(color.white, piece_const.PieceValues()), -3)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.PieceValues()), 3)

        self.board = Board.init_default()
        self.board.position[7][0] = None

        self.assertEqual(self.board.material_advantage(color.white, piece_const.PieceValues()), 5)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.PieceValues()), -5)

        self.board = Board.init_default()
        self.board.position[7][3] = None

        self.assertEqual(self.board.material_advantage(color.white, piece_const.PieceValues()), 9)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.PieceValues()), -9)

        self.board = Board.init_default()
        self.board.position[7][2] = None

        self.assertEqual(self.board.material_advantage(color.white, piece_const.PieceValues()), 3.5)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.PieceValues()), -3.5)

    def test_advantage_as_result(self):
        self.assertEqual(self.board.advantage_as_result(converter.long_alg("e2e4", self.board),
                                                        piece_const.PieceValues()), 0)

        self.board.position[1][3] = None
        self.assertEqual(
            self.board.advantage_as_result(converter.long_alg("d1d7", self.board), piece_const.PieceValues()), 0)

        self.board.update(converter.short_alg("e3", color.white, self.board))

        self.assertEqual(
            self.board.advantage_as_result(
                converter.short_alg("Bd2", color.white, self.board), piece_const.PieceValues()), -1)

    def test_all_possible_moves_1(self):
        """
        Print statement to easily get the list of moves in string form.
        Used for constructing tests.

        for move in self.board.all_possible_moves(color.white):
            print("\""+ str(move) + "\", ", end="")
        """
        moves = {"b1c3", "b1a3", "g1h3", "g1f3", "a2a3", "a2a4", "b2b3", "b2b4",
                 "c2c3", "c2c4", "d2d3", "d2d4", "e2e3", "e2e4", "f2f3", "f2f4",
                 "g2g3", "g2g4", "h2h3", "h2h4"}

        self.assertEqual(moves, {str(move) for move in self.board.all_possible_moves(color.white)})

    def test_all_possible_moves_2(self):
        self.board.update(converter.long_alg("e2e4", self.board))

        moves = {"a7a6", "a7a5", "b7b6", "b7b5", "c7c6", "c7c5", "d7d6", "d7d5",
                 "e7e6", "e7e5", "f7f6", "f7f5", "g7g6", "g7g5", "h7h6", "h7h5",
                 "b8a6", "b8c6", "g8f6", "g8h6"}

        self.assertEqual(moves, {str(move) for move in self.board.all_possible_moves(color.black)})

    def test_no_moves(self):
        self.assertFalse(self.board.no_moves(color.white))
        self.assertFalse(self.board.no_moves(color.black))

        self.board.update(converter.short_alg("f4", color.white, self.board))
        print(self.board)
        self.board.update(converter.short_alg("e5", color.black, self.board))
        self.board.update(converter.short_alg("g4", color.white, self.board))
        self.board.update(converter.short_alg("Qh4", color.black, self.board))

        self.assertTrue(self.board.no_moves(color.white))

    def test_find_piece(self):
        self.assertEqual(self.board.find_piece(Rook(color.white, Location(0, 0))),
                          Location(0, 0))

        self.assertEqual(self.board.find_piece(Rook(color.black, Location(7, 0))),
                          Location(7, 0))

        self.assertNotEqual(self.board.find_piece(Rook(color.black, Location(7, 0))),
                             Location(3, 0))

        self.assertEqual(self.board.find_piece(Pawn(color.white, Location(0, 0))),
                         Location.from_string("a2"))

        self.assertEqual(self.board.find_piece(Knight(color.white, Location(0, 0))),
                         Location.from_string("b1"))

    def test_find_king(self):
        self.assertEqual(self.board.find_king(color.white),
                          Location(0, 4))

        self.assertEqual(self.board.find_king(color.black),
                          Location(7, 4))

    def test_get_king(self):
        self.assertEqual(self.board.get_king(color.white),
                          King(color.white, Location(0, 4)))

        self.assertEqual(self.board.get_king(color.black),
                          King(color.black, Location(7, 4)))

    def test_remove_piece_at_square(self):
        test_board = Board.init_default()
        test_board.position[0][0] = None
        self.board.remove_piece_at_square(Location(0, 0))
        self.assertEqual(self.board, test_board)

    def test_place_piece_at_square(self):
        test = Board.init_default()
        pawn = Pawn(color.white, Location.from_string("e3"))

        test.position[2][4] = pawn

        self.board.place_piece_at_square(pawn, Location.from_string("e3"))

        self.assertEqual(self.board, test)

    def test_move_piece(self):
        test = Board.init_default()
        pawn = test.position[1][4]
        test.position[1][4] = None
        test.position[3][4] = pawn

        self.board.move_piece(Location.from_string("e2"), Location.from_string("e4"))

        self.assertEqual(self.board, test)

    def test_update(self):
        test = Board.init_default()
        pawn = test.position[1][4]
        test.position[1][4] = None
        test.position[3][4] = pawn

        self.board.update(converter.long_alg("e2e4", self.board))

        self.assertEqual(self.board, test)
