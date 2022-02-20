import math


def main(n):
    f0 = 0.33
    f1 = -0.62
    if n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        return math.tan(main(n-2)) ** 3 + main(n-1)
