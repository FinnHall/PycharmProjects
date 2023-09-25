from unittest import TestCase


def load_booklist():
    list = []
    with open('booklist.txt', 'r') as booklist_file:
        row = booklist_file.read().splitlines()
    for i in row:
        list.append(tuple(i.split(',')))
    return list


def ReadersRatingsDictionary():
    with open("ratings.txt") as ratings_file:
        data = ratings_file.read().splitlines()
        names = data[::2]
        ratings = [list(map(int, ratings.split())) for ratings in data[1::2]]
        Dict = dict(list(zip(names, ratings)))
        return Dict


def correlationIndex(a, b):
    c = 0
    for i in range(len(a)):
        c += a[i] * b[i]
    return c


def calculate(name, Dict, correlation):
    final = {}
    person = Dict[name]
    Dict.pop(name)
    for i in Dict.keys():
        result = correlation(person, (Dict[i]))
        final[i] = result
        return final


def final_two(final):
    sort = (sorted(final, key=lambda x: x[1], reverse=True))
    two = ([i[0] for i in sort[:2:]])
    return two


# def reco_Books(reader, similar_readers, Dict, list):
#
#     for i in range(len(list)):
#         if main_user_rating[i]
#
#     pass


