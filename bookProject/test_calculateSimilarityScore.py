from unittest import TestCase
from calculateSimilarityScore import *

class calculate(TestCase):
    def test_calculate(self):
        val = calculate(Ben, Dict, correlation)
        self.assertEqual(75, val, f'Something failed calculating {val} for [5, 5, 5], [10, 2, 3]')
