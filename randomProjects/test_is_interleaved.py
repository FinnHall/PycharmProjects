from unittest import TestCase
from is_interleaved import *

class TestIsInterleaved(TestCase):
    def test_is_interleaved(self):
        self.assertFalse(is_interleaved("XXY", "XXZ", "XXZXXXY"))
        self.assertTrue(is_interleaved("XY", "WZ", "WZXY"))
        self.assertTrue(is_interleaved("XY", "X", "XXY"))
        self.assertFalse(is_interleaved("YX", "X", "XXY"))
        self.assertTrue(is_interleaved("XXY", "XXZ", "XXXXZY"))


# "XXY", "XXZ", "XXZXXXY"
# "XY", "WZ", "WZXY"
# "XY", "X", "XXY"
# "YX", "X", "XXY"
# "XXY", "XXZ", "XXXXZY"
