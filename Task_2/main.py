def main(y):
    if y < 65:
        return 88 * y ** 3 + (70 * y ** 2 - 1 - 65 * y) ** 4
    elif 65 <= y < 78:
        return ((74 * y ** 3 + 0.2 + y) ** 5) / 8 - 55
    elif 78 <= y < 108:
        return 24 * y ** 2 + 30 * (1 + y ** 3 + 67 * y ** 2)
    elif y >= 108:
        return y ** 2 + 61 * ((77 * y ** 2 - y) ** 7)
