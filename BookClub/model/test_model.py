from unittest import TestCase
from model import calc_similarity_score, find_two_most_similar_members, create_recommended_booklist

def test_correlation_calculator(list1, list2):
    # a simple calculation here for testing purposes
    # change as desired, but the calculations have to be local, may not dependent on some external library
    return sum(list1) + sum(list2)


class TestCalcSimilarityScore(TestCase):
    def test_calc_similarity_score(self):
        member_ratings = {
            "Priscilla": [5, 0, 0, 0, 0, 0, 5],
            "Harry Potter": [0, 0, 0, 0, 0, 0, 0],
            "Apollo": [0, 0, 0, -3, 0, 0, 0],
            "Jaluka": [0, 5, 0, 0, 0, 0, 0],
            "Martin": [1, -3, 0, 0, 0, 0, 0]
        }
        entered_member = "Martin"
        member_and_rating_list = calc_similarity_score(entered_member, member_ratings,  test_correlation_calculator)
        self.assertTrue(("Priscilla", 8) in member_and_rating_list)
        self.assertTrue(("Harry Potter", -2) in member_and_rating_list)
        self.assertTrue(("Apollo", -5) in member_and_rating_list)
        self.assertTrue(("Jaluka", 3) in member_and_rating_list)
        self.assertTrue(("Martin", -4) not in member_and_rating_list)
        self.assertEqual(4, len(member_and_rating_list))

    def test_calc_similarity_score2(self):
        # not it's your turn - create a test case
        pass

    def test_calc_similarity_score3(self):
        # not it's your turn - create a test case
        pass

class TestFindTwoMostSimilarMembers(TestCase):
    def test_find_two_most_similar_members(self):
        data = (("Priscilla", 10), ("Carlos", 12), ("Ethan", 8), ("Sue", 16))
        result = find_two_most_similar_members(data)
        self.assertTrue("Sue" in result)
        self.assertTrue("Carlos" in result)
        self.assertEquals(2, len(result))

    def test_find_two_most_similar_top_three_same_value(self):
        # your turn, create a test case
        pass

    def test_find_two_most_similar_second_top_two_same_value(self):
        # your turn, create a test case
        pass

class TestCreateRecommendedBooklist(TestCase):
    def test_create_recommended_booklist(self):
        ratings_martin = [1, -3, 0, 0, 0, 0, 0]
        ratings_apollo = [0, 0, 0, -3, 0, 0, 0]
        ratings_priscilla = [5, 0, 0, 0, 0, 0, 5]
        booklist = (
            ("Douglas Adams", "The Hitchhiker's Guide To The Galaxy"),
            ("Richard Adams", "Watership Down"),
            ("Mitch Albom", "The Five People You Meet in Heaven"),
            ("Laurie Halse Anderson", "Speak"),
            ("Maya Angelou", "I Know Why the Caged Bird Sings"),
            ("Jay Asher", "Thirteen Reasons Why"),
            ("Isaac Asimov", "Foundation Series")
        )
        # now write the test

    def test_create_recommended_booklist2(self):
        # your turn, create a test case
        pass

    def test_create_recommended_booklist3(self):
        # your turn, create a test case
        pass

