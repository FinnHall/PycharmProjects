from data.file_data_import import *
from view.view import *
from model.model import *
from correlation import *


def main():
    booklist = load_booklist()
    all_members_ratings = load_member_ratings()

    again = "Y"
    while again == "Y":
        name = query_user_for_member(all_members_ratings.keys())
        if name is not None:
            member_and_rating_list = calc_similarity_score(name, all_members_ratings, dot_product)
            similar_members = find_two_most_similar_members(member_and_rating_list)
            recommended_booklist = create_recommended_booklist(
                all_members_ratings[name],
                all_members_ratings[similar_members[0]],
                all_members_ratings[similar_members[1]],
                booklist)
            print_recommendations(name, similar_members, recommended_booklist)
        again = input("Create another recommended booklist? (Y/N): ")


if __name__ == '__main__':
    main()