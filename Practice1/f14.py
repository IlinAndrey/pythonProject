import math


def f14(n):
    if n == 0:
        return 10
    else:
        return 1 / 49 * ((f14(n - 1)) ** 2) - math.tan(f14(n - 1)) - 38
