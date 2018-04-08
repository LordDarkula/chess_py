from unittest import TestCase

from chess_py import color


class TestColor(TestCase):

    def test_opponent(self):
        self.assertEqual(-color.white, color.black)
        self.assertEqual(-color.black, color.white)
