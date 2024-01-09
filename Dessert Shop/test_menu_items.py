from unittest import TestCase
from menu_items import Candy, Cookies


class TestCandy(TestCase):
    def test_cost(self):
        candy = Candy(.25)
        self.assertEqual(1.5625, candy.cost())


class TestCookies(TestCase):
    def test_cost(self):
        cookies = Cookies(50)
        self.assertEqual(312.5, cookies.cost())
