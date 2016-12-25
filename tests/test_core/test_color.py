from unittest import TestCase

from chess_py import color


class TestColor(TestCase):
    def test_pwhite(self):
        self.assertEqual(color.Color.pwhite(), color.white, color.Color("white"))

    def test_pblack(self):
        self.assertEqual(color.Color.pblack(), color.black, color.Color("black"))

    def test_opponent(self):
        self.assertEqual(color.white.opponent(), color.black)
        self.assertEqual(color.black.opponent(), color.white)
