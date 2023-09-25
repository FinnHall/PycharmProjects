from calculateSimilarityScore import final_two
from unittest import TestCase


class FinalTwoTest(TestCase):

    def test_final_two(self):
        members = final_two((("Billy", 10), ("Ted", 7), ("Fred", 0), ("Bread", 15)))
        self.assertEqual(members, ['Bread', 'Billy'])

    def test_final_two_1(self):
        members = final_two((("Tammy", 0), ("Ned", 10), ("Tread", 100), ("Bed", 50)))
        self.assertEqual(members, ['Tread', 'Bed'])

    def test_final_two_2(self):
        members = final_two((("Valentina", -5000000), ("Bill", 98231), ("Bob", 1000), ("Jebadiah", 100000000)))
        self.assertEqual(members, ['Jebadiah', 'Bill'])

    def test_final_two_3(self):
        members = final_two((("Jared", 93), ("Kyle", 78), ("Mr. Lee", 145), ("Potter", 123)))
        self.assertEqual(members, ['Mr. Lee', 'Potter'])

    def test_final_two_4(self):
        members = final_two((("Car", 435), ("Kory", 123), ("Tilda", 643), ("Eugene", 231)))
        self.assertEqual(members, ['Tilda', 'Car'])
