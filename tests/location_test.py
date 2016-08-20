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

if __name__ == '__main__':
    unittest.main()
