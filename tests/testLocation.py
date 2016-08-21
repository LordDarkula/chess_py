import unittest
from chess_py import Location


class LocationTest(unittest.TestCase):

    def testEquals(self):
        self.failUnless(Location(8, 8).equals(Location(8, 8)))
        self.failUnless(Location(2, 3).equals(Location(2, 3)))
        self.failUnless(Location(7, 6).equals(Location(7, 6)))
        self.failIf(Location(4, 5).equals(Location(5, 4)))

    def testOnBoard(self):
        self.failUnless(Location(3, 4).on_board())
        self.failIf(Location(8, 7).on_board())
        self.failIf(Location(4, 8).on_board())
        self.failIf(Location(8, 4).on_board())

    def testShiftUp(self):
        self.failUnless(Location(3, 4).shift_up().equals(Location(4, 4)))
        self.failUnless(Location(0, 2).shift_up().equals(Location(1, 2)))

    def testShiftDown(self):
        self.failUnless(Location(3, 4).shift_down().equals(Location(2, 4)))
        self.failUnless(Location(1, 2).shift_down().equals(Location(0, 2)))

    def testShiftRight(self):
        self.failUnless(Location(3, 4).shift_right().equals(Location(3, 5)))
        self.failUnless(Location(0, 2).shift_right().equals(Location(0, 3)))

    def testShiftLeft(self):
        self.failUnless(Location(3, 4).shift_left().equals(Location(3, 3)))
        self.failUnless(Location(0, 2).shift_left().equals(Location(0, 1)))

if __name__ == '__main__':
    unittest.main()
