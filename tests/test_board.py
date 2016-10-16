from unittest import TestCase
from chess_py import color, Location, Board, Pawn, Knight, Bishop, Rook, Queen, King, piece_const, converter


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board.init_default()

    def test_init_default(self):
        white = color.white
        black = color.black
        self.assertEqual(self.board, Board([

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
         Knight(black, Location(7, 6)), Rook(black, Location(7, 7))]]))

    def test_copy(self):
        tester = Board.init_default()

        for num, row in enumerate(self.board.position):
            for index, piece in enumerate(row):
                self.assertEquals(piece, tester.position[num][index])

    def test_piece_at_square(self):
        self.assertEquals(self.board.piece_at_square(Location(0, 0)),
                          Rook(color.white, Location(0, 0)))

        self.assertEquals(self.board.piece_at_square(Location(1, 0)),
                          Pawn(color.white, Location(1, 0)))

        self.assertEquals(self.board.piece_at_square(Location(0, 1)),
                          Knight(color.white, Location(0, 1)))

    def test_is_square_empty(self):
        self.failUnless(self.board.is_square_empty(Location(2, 0)))
        self.failIf(self.board.is_square_empty(Location(0, 3)))

    def test_material_advantage(self):
        self.assertEqual(self.board.material_advantage(color.white, piece_const.Piece_values()), 0)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.Piece_values()), 0)

        self.board.position[0][0] = None

        self.assertEqual(self.board.material_advantage(color.white, piece_const.Piece_values()), -5)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.Piece_values()), 5)

        self.board = Board.init_default()
        self.board.position[0][1] = None

        self.assertEqual(self.board.material_advantage(color.white, piece_const.Piece_values()), -3)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.Piece_values()), 3)

        self.board = Board.init_default()
        self.board.position[7][0] = None

        self.assertEqual(self.board.material_advantage(color.white, piece_const.Piece_values()), 5)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.Piece_values()), -5)

        self.board = Board.init_default()
        self.board.position[7][3] = None

        self.assertEqual(self.board.material_advantage(color.white, piece_const.Piece_values()), 9)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.Piece_values()), -9)

        self.board = Board.init_default()
        self.board.position[7][2] = None

        self.assertEqual(self.board.material_advantage(color.white, piece_const.Piece_values()), 3)
        self.assertEqual(self.board.material_advantage(color.black, piece_const.Piece_values()), -3)

    def test_advantage_as_result(self):
        self.assertEqual(self.board.advantage_as_result(converter.long_alg("e2e4", self.board), piece_const.Piece_values()), 0)

        self.board.position[1][3] = None
        self.assertEqual(self.board.advantage_as_result(converter.long_alg("d1d7", self.board),
                                                    piece_const.Piece_values()), 0)

        self.board.update(converter.short_alg("e3", color.white, self.board))

        self.assertEqual(self.board.advantage_as_result(converter.short_alg("Bd2", color.white, self.board),
                                                        piece_const.Piece_values()), -1)

    def test_all_possible_moves(self):
        self.fail()

    def test_find_piece(self):
        self.assertEquals(self.board.find_piece(Rook(color.white, Location(0, 0))),
                          Location(0, 0))

        self.assertEquals(self.board.find_piece(Rook(color.black, Location(7, 0))),
                          Location(7, 0))

        self.assertNotEquals(self.board.find_piece(Rook(color.black, Location(7, 0))),
                             Location(3, 0))

        self.assertEqual(self.board.find_piece(Pawn(color.white, Location(0, 0))),
                         Location.init_alg("a2"))

        self.assertEqual(self.board.find_piece(Knight(color.white, Location(0, 0))),
                         Location.init_alg("b1"))

    def test_find_king(self):
        self.assertEquals(self.board.find_king(color.white),
                          Location(0, 4))

        self.assertEquals(self.board.find_king(color.black),
                          Location(7, 4))

    def test_get_king(self):
        self.assertEquals(self.board.get_king(color.white),
                          King(color.white, Location(0, 4)))

        self.assertEquals(self.board.get_king(color.black),
                          King(color.black, Location(7, 4)))

    def test_remove_piece_at_square(self):
        test_board = Board.init_default()
        test_board.position[0][0] = None
        self.board.remove_piece_at_square(Location(0, 0))
        self.assertEqual(self.board, test_board)

    def test_place_piece_at_square(self):
        self.fail()

    def test_move_piece(self):
        self.fail()

    def test_update(self):
        self.fail()
