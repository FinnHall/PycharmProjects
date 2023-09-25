
def poop(pee, poo):
    peee = 0
    for p in range(len(pee)):
        peee += pee[p] * poo[p]
    return peee


assert poop([1, 2, 5], [3, 3, 3]) == 24
assert poop([1, 1, 1], [1, 1, 1]) == 3
assert poop([10, 20, 50], [10, 10, 10]) == 800
assert poop([50, 2, 1000], [1, 100, 1000]) == 1000250
assert poop([45, 20, 2], [4, 8, 16]) == 372


