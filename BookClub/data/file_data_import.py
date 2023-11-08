

def load_booklist():
    booklist = []
    with open('data/booklist.txt', 'r') as booklist_file:
        row = booklist_file.read().splitlines()
    for i in row:
        booklist.append(tuple(i.split(',')))
    return booklist


def load_member_ratings():
    with open("data/ratings.txt") as ratings_file:
        data = ratings_file.read().splitlines()
        names = data[::2]
        ratings = [list(map(int, ratings.split())) for ratings in data[1::2]]
        all_members_ratings = dict(list(zip(names, ratings)))
        return all_members_ratings

