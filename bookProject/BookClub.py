from unittest import TestCase

def load_booklist():
    book_list = []
    with open('booklist.txt', 'r') as booklist_file:
        row = booklist_file.read().splitlines()
    for i in row:
        book_list.append(tuple(i.split(',')))
    return book_list


def ReadersRatingsDictionary():
    with open("ratings.txt") as ratings_file:
        data = ratings_file.read().splitlines()
        names = data[::2]
        ratings = [list(map(int, ratings.split())) for ratings in data[1::2]]
        rating_dict = dict(list(zip(names, ratings)))
        return rating_dict


def correlationIndex(a, b):
    c = 0
    for i in range(len(a)):
        c += a[i] * b[i]
    return c


def calculate(name, rating_dict, correlation):
    score = {}
    person = rating_dict[name]
    rating_dict.pop(name)
    for i in rating_dict.keys():
        result = correlation(person, (rating_dict[i]))
        score[i] = result
    return score


def final_two(score):
    sort = (sorted(score, key=lambda x: x[1], reverse=True))
    two = ([i[0] for i in sort[:2:]])
    return two




def reco_books(reader, two, rating_dict, book_list):
    reco_list = []
    reader1 = rating_dict[reader]
    reader2 = rating_dict[two[0]]
    reader3 = rating_dict[two[1]]
    for i in range(len(book_list)):
        if reader1[i] == 0 and (reader2[i] >= 3 or reader3[i] >= 3):
            reco_list.append(book_list[i])
    return reco_list


#reco_books('Moose', ('Mike', 'Ella'), ReadersRatingsDictionary(), load_booklist())



# reco_books(input('Member Name: '))
            #add book at i to the recommended list

#print(final_two(calculate('Leah', ReadersRatingsDictionary(), correlationIndex).items()))
#print(reco_books('Leah', ['Iren', 'hidan'], ReadersRatingsDictionary(), load_booklist()
