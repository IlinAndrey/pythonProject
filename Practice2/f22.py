def f22(x):
    a = x & 0b1111111111111
    x >>= 13
    a <<= 4
    b = x & 0b111111111111111
    x >>= 15
    b <<= 17
    c = x & 0b1111
    x >>= 4
    c <<= 0
    return a + b + c


print(hex(f22(0xf29317b3)))