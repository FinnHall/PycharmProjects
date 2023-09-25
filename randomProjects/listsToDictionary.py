
def combine(poo, pee):
    combine = {}
    for p in range(len(poo)):
        combine[poo[p]] = pee[p]
    return combine


assert combine([1, 2, 3, 4, 5], ["p", "pp", "ppp", "pppp", "ppppp"]) \
       == {1: 'p', 2: 'pp', 3: 'ppp', 4: 'pppp', 5: 'ppppp'}
