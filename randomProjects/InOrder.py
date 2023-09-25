
def inOrder(a, b ,c, bOk):
    if c > a and bOk:
        return True
    elif bOk == False and c > b > a:
        return True
    else:
        return False

assert inOrder(1, 2, 4, False) == True
assert inOrder(1, 2, 1, False) == False
assert inOrder(1, 1, 2, True) == True
