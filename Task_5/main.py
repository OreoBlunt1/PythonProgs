def main(z, y):
    res = 0
    for i in range(1, len(z)+1):
        res += (y[i-1] ** 3 + 77 * z[i-1] + 1) ** 5
    return 63 * res
