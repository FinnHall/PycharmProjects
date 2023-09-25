def calc_similarity_score(member, all_members_ratings, correlation_calculator):
    pass


def find_two_most_similar_members(member_and_rating_list):
    sort = (sorted(member_and_rating_list, key=lambda x: x[1], reverse=True))
    return [i[0] for i in sort[:2:]]


def create_recommended_booklist(entered_member_ratings, similar_member1_ratings, similar_member2_ratings, booklist):
    recommended_books = []
    for i in range(len(booklist)):
        if entered_member_ratings[i] == 0 and (similar_member1_ratings[i] >= 3 or similar_member2_ratings[i] >= 3):
            recommended_books.append(booklist[i])
        return recommended_books


