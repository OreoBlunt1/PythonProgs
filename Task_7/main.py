def main(lol):
    a = lol & 0b1111_1111_111
    b = (lol >> 11) & 0b1111_1111_1
    c = (lol >> 20) & 0b1111_1111
    d = (lol >> 28) & 0b1111
    result = a | (d << 11) | (b << 15) | (c << 24)
    return result
