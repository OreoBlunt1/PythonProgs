import math


def main(n, b, m):
    res1 = 0
    res2 = 0
    for c in range(1, b+1):
        for k in range(1, n+1):
            res1 += 90 * (94 * k ** 3 + 1 + c) ** 2
    for c in range(1, n+1):
        for j in range(1, m+1):
            res2 += math.log(97 * j ** 2) ** 7 -\
                    ((c + 82 * j ** 2) ** 2) / 55 - 65
    return res1 + res2
