from unittest import TestCase
from test import *


class Test_octal_decimal(TestCase):
    def test_octal_decimal(self):
        number = 35678970987356
        octl = oct(number)
        self.assertEqual(number, octal_decimal(octl))
