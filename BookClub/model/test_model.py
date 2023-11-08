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
        member_ratings = {
            "Guy": [5, 0, 2, 0, 4, 0, 5],
            "Other Guy": [1, -2, 3, 0, 4, -1, 0],
            "Steve": [3, 0, -1, -3, 0, -2, 0],
            "Han": [1, 2, 3, 4, 5, -5, -4],
            "Van Buren": [2, -3, 4, 0, 3, 0, 1]
        }
        entered_member = "Han"
        member_and_rating_list = calc_similarity_score(entered_member, member_ratings, test_correlation_calculator)
        self.assertTrue(("Guy", 22) in member_and_rating_list)
        self.assertTrue(("Other Guy", 11) in member_and_rating_list)
        self.assertTrue(("Steve", 3) in member_and_rating_list)
        self.assertTrue(("Han", 6) not in member_and_rating_list)
        self.assertTrue(("Van Buren", 13) in member_and_rating_list)
        self.assertEqual(4, len(member_and_rating_list))

    def test_calc_similarity_score3(self):
        member_ratings = {
            "Name": [0, 5, 2, 0, 0, 4, 5],
            "Yeah": [0, -2, 3, 1, 0, -1, 4],
            "Uhm": [-1, 0, 3, -2, 0, -3, 0],
            "Yessir": [-5, 3, 2, -4, 5, 1, 4],
            "Help": [0, 3, 4, 0, -3, 2, 1]
        }
        entered_member = "Uhm"
        member_and_rating_list = calc_similarity_score(entered_member, member_ratings, test_correlation_calculator)
        self.assertTrue(("Name", 13) in member_and_rating_list)
        self.assertTrue(("Yeah", 2) in member_and_rating_list)
        self.assertTrue(("Uhm", -3) not in member_and_rating_list)
        self.assertTrue(("Yessir", 3) in member_and_rating_list)
        self.assertTrue(("Help", 4) in member_and_rating_list)
        self.assertEqual(4, len(member_and_rating_list))


class TestFindTwoMostSimilarMembers(TestCase):
    def test_find_two_most_similar_members(self):
        data = (("Priscilla", 10), ("Carlos", 12), ("Ethan", 8), ("Sue", 16))
        result = find_two_most_similar_members(data)
        self.assertTrue("Sue" in result)
        self.assertTrue("Carlos" in result)
        self.assertEqual(2, len(result))

    def test_find_two_most_similar_top_three_same_value(self):
        data = (("Joshua", 3), ("Bo Biden", 8), ("Horace Mann", 4), ("Tilda", 6))
        result = find_two_most_similar_members(data)
        self.assertTrue("Bo Biden" in result)
        self.assertTrue("Tilda" in result)
        self.assertEqual(2, len(result))
        pass

    def test_find_two_most_similar_second_top_two_same_value(self):
        data = (("Charles", 6), ("Kim", 7), ("Jon", 3), ("Clark", 21))
        result = find_two_most_similar_members(data)
        self.assertTrue("Clark" in result)
        self.assertTrue("Kim" in result)
        self.assertEqual(2, len(result))
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
        recommended_booklist = create_recommended_booklist(ratings_martin, ratings_priscilla, ratings_apollo, booklist)
        self.assertTrue(("Isaac Asimov", "Foundation Series") in recommended_booklist)

    def test_create_recommended_booklist2(self):
        ratings_ted = [1, 4, 0, -2, 0, 3, 0]
        ratings_bill = [0, 2, 5, -2, 0, 4, 0]
        ratings_dued = [3, 0, 5, 0, -3, 0, 5]
        booklist = (
            ("Douglas Adams", "The Hitchhiker's Guide To The Galaxy"),
            ("Richard Adams", "Watership Down"),
            ("Mitch Albom", "The Five People You Meet in Heaven"),
            ("Laurie Halse Anderson", "Speak"),
            ("Maya Angelou", "I Know Why the Caged Bird Sings"),
            ("Jay Asher", "Thirteen Reasons Why"),
            ("Isaac Asimov", "Foundation Series")
        )
        recommended_booklist = create_recommended_booklist(ratings_ted, ratings_bill, ratings_dued, booklist)
        self.assertTrue(("Mitch Albom", "The Five People You Meet in Heaven") in recommended_booklist)

    def test_create_recommended_booklist3(self):
        ratings_nick = [1, 3, -2, 5, 0, 4, 3]
        ratings_lucy = [-3, 1, 3, -1, 4, -1, 2]
        ratings_jackson = [-2, 0, 1, 0, 5, 2, 1]
        booklist = (
            ("Douglas Adams", "The Hitchhiker's Guide To The Galaxy"),
            ("Richard Adams", "Watership Down"),
            ("Mitch Albom", "The Five People You Meet in Heaven"),
            ("Laurie Halse Anderson", "Speak"),
            ("Maya Angelou", "I Know Why the Caged Bird Sings"),
            ("Jay Asher", "Thirteen Reasons Why"),
            ("Isaac Asimov", "Foundation Series")
        )
        recommended_booklist = create_recommended_booklist(ratings_nick, ratings_lucy, ratings_jackson, booklist)
        self.assertTrue(("Maya Angelou", "I Know Why the Caged Bird Sings") in recommended_booklist)

