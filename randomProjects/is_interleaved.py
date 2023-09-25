def is_interleaved(a, b, c):
    m = len(a)
    n = len(b)

    il = [[False] * (n + 1) for i in range(m + 1)]
    if (m + n) != len(c):
        return False
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if i == 0 and j == 0:
                il[i][j] = True
            elif i == 0:
                if b[j - 1] == c[j - 1]:
                    il[i][j] = il[i][j - 1]
            elif j == 0:
                if a[i - 1] == c[i - 1]:
                    il[i][j] = il[i - 1][j]

            elif (a[i - 1] == c[i + j - 1] and
                  b[j - 1] != c[i + j - 1]):
                il[i][j] = il[i - 1][j]

            elif (a[i - 1] != c[i + j - 1] and
                  b[j - 1] == c[i + j - 1]):
                il[i][j] = il[i][j - 1]

            elif (a[i - 1] == c[i + j - 1] and
                  b[j - 1] == c[i + j - 1]):
                il[i][j] = (il[i - 1][j] or il[i][j - 1])
    return il[m][n]
