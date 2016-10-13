import unittest
from chess_py import Board, Location, Pawn, Knight, Rook, King, color


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board.init_default()

    def testCopy(self):
        tester = Board.init_default()

        for num, row in enumerate(self.board.position):
            for index, piece in enumerate(row):
                self.assertEquals(piece, tester.position[num][index])

    def testPieceAtSquare(self):
        self.assertEquals(self.board.piece_at_square(Location(0, 0)),
                          Rook(color.white, Location(0, 0)))

        self.assertEquals(self.board.piece_at_square(Location(1, 0)),
                          Pawn(color.white, Location(1, 0)))

        self.assertEquals(self.board.piece_at_square(Location(0, 1)),
                          Knight(color.white, Location(0, 1)))

    def testIsSquareEmpty(self):
        self.failUnless(self.board.is_square_empty(Location(2, 0)))
        self.failIf(self.board.is_square_empty(Location(0, 3)))

    def testFindPiece(self):
        self.assertEquals(self.board.find_piece(Rook(color.white, Location(0, 0))),
                          Location(0, 0))

        self.assertEquals(self.board.find_piece(Rook(color.black, Location(7, 0))),
                          Location(7, 0))

        self.assertNotEquals(self.board.find_piece(Rook(color.black, Location(7, 0))),
                             Location(3, 0))

    def testFindKing(self):
        self.assertEquals(self.board.find_king(color.white),
                          Location(0, 4))

        self.assertEquals(self.board.find_king(color.black),
                          Location(7, 4))

    def testGetKing(self):
        self.assertEquals(self.board.get_king(color.white),
                          King(color.white, Location(0, 4)))

        self.assertEquals(self.board.get_king(color.black),
                          King(color.black, Location(7, 4)))
