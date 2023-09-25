
def ReadersRatingsDictionary():
    Dict = {}
    with open("ratings.txt") as ratings_file:
        data = ratings_file.read().splitlines()
        names = data[::2]
        ratings = data[1::2]
        for i in range(len(names)):
            Dict[names[i]] = ratings[i]
        return Dict


print(ReadersRatingsDictionary())

