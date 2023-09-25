
def sum_array(array):

    array_sum = 0
    i = 0
    while i < len(array):
        if array[i] == 13:
            i += 2
        else:
            array_sum += array[i]
            i += 1

    return array_sum

assert sum_array([1, 2, 3, 13, 2, 3]) == 9
assert sum_array([0]) == 0
assert sum_array([1100, 45, 13, 1000000000000, 1, 420]) == 1579
