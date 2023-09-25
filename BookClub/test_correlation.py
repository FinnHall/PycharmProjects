from unittest import TestCase
from correlation import dot_product

class TestDotProduct(TestCase):
    def test_dot_product1(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        c = dot_product(a, b)
        self.assertEqual(14, c)

    def test_dot_product2(self):
        a = [5, 3, -5]
        b = [5, -3, 5]
        c = dot_product(a, b)
        self.assertEqual(-9, c)

    def test_dot_product3(self):
        a = [2, 14, 3, 6]
        b = [5, 4, 9, -3]
        c = dot_product(a, b)
        self.assertEqual(75, c)

