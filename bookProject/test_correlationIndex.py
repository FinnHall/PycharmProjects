from unittest import TestCase
from calculateSimilarityScore import *

class Test_CorrelationIndex(TestCase):
    def test_correlation_index(self):
        val = correlationIndex([5, 5, 5], [10, 2, 3])
        self.assertEqual(75, val, f'Something failed calculating {val} for [5, 5, 5], [10, 2, 3]')
        val = correlationIndex([5, 5, 5], [5, 5, 5])
        self.assertEqual(75, val, f'Something failed calculating {val} for [5, 5, 5], [5, 5, 5]')
        val = correlationIndex([1, 1, 1], [1, 1, 1])
        self.assertEqual(3, val, f'Something failed calculating {val} for [1, 1, 1], [1, 1, 1]')

    def final_two(self):
        val = final_two((("Linda", 100), ("Brad", 0), ("Tilda", 20)))
        self.assertEqual(['Linda', 'Tilda'], val, f'Something failed calculating {val} for ("Linda", 100), ("Brad", 0), ("Tilda", 20)')
        val = final_two((("Herman", 5), ("Kad", 10), ("Manber", 0)))
        self.assertEqual(['Kad', 'Herma'], val, f'Something failed calculating {val} for ("Herman", 5), ("Kad", 10), ("Manber", 0)')
        val = final_two((("Jebadiah", 9999), ("Bill", 0), ("Bob", 100), ("Valentina", -1000000)))
        self.assertEqual(['Jebadiah', 'Bob'], val, f'Something failed calculating {val} for ("Jebadiah", 9999), ("Bill", 0), ("Bob", 100), ("Valentina", -1000000)')
