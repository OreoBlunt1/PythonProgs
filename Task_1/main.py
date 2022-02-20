import math


def main(z, y):
    x = abs(1-z) ** 7
    n = 56 * (math.sin((y ** 3 / 75) - 1) ** 6)
    m = math.sqrt(((z ** 3 / 72) + 5 * y ** 2 + 74 * z) ** 7 +
                  (y + 88 * y ** 2 + 1) ** 5)
    return x + n - m
