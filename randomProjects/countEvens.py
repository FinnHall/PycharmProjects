
def countEvens(list):
    evens = 0
    for f in list:
        if f % 2 == 0:
            evens += 1
    return evens


assert countEvens([2, 1, 2, 3, 4]) == 3
assert countEvens([2, 2, 0]) == 3
assert countEvens([1, 3, 5]) == 0
