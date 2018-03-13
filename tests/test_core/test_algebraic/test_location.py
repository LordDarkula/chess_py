import unittest

from chess_py import Location


class TestLocation(unittest.TestCase):

    def testEquals(self):
        self.assertEqual(Location(2, 3), Location(2, 3))
        self.assertEqual(Location(7, 6), Location(7, 6))
        self.assertNotEqual(Location(4, 5), Location(5, 4))

    def testStr(self):
        self.assertEqual(str(Location(3, 4)), "e4")
        self.assertEqual(str(Location(0, 0)), "a1")
        self.assertEqual(str(Location(7, 7)), "h8")

    def testShiftUp(self):
        self.assertEqual(Location(3, 4).shift_up(), Location(4, 4))
        self.assertEqual(Location(0, 2).shift_up(), Location(1, 2))

    def testShiftDown(self):
        self.assertEqual(Location(3, 4).shift_down(), Location(2, 4))
        self.assertEqual(Location(1, 2).shift_down(), Location(0, 2))

    def testShiftRight(self):
        self.assertEqual(Location(3, 4).shift_right(), Location(3, 5))
        self.assertEqual(Location(0, 2).shift_right(), Location(0, 3))

    def testShiftLeft(self):
        self.assertEqual(Location(3, 4).shift_left(), Location(3, 3))
        self.assertEqual(Location(0, 2).shift_left(), Location(0, 1))

    def testShiftUpRight(self):
        self.assertEqual(Location(3, 4).shift_up_right(), Location(4, 5))

    def testShiftUpLeft(self):
        self.assertEqual(Location(1, 2).shift_up_left(), Location(2, 1))

    def testShiftDownRight(self):
        self.assertEqual(Location(5, 3).shift_down_right(), Location(4, 4))

    def testShiftDownLeft(self):
        self.assertEqual(Location(1, 1).shift_down_left(), Location(0, 0))

if __name__ == '__main__':
    unittest.main()
