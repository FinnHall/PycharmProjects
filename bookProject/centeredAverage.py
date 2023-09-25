
def centered_average(pee):
    poo = pee[1:-1]
    poop = sum(poo)//len(poo)
    return poop

assert centered_average([1, 2, 3, 4, 100]) == 3
assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
assert centered_average([-10, -4, -2, -4, -2, 0]) == -3
