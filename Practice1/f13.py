import math


def f13(n):
    s1 = 0
    for i in range(1, n + 1):
        s1 += ((6 * (i ** 2)) - (7 * (i ** 4)))

    s2 = 0
    for i in range(1, n + 1):
        s2 += (math.sin(i) - math.fabs(i) - 19)

    return 14 * s1 + 60 * s2

