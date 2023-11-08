final = 0
for i in range(len(str(oct(31))) - 1):
    final += (int(str(oct(31))[-i]) * (8 ** (i-1)))


def octal_decimal(number):
    decimal = 0
    for i in range(len(str(number)) - 1):
        decimal += (int(str(number)[-i]) * (8 ** (i - 1)))
    return decimal

