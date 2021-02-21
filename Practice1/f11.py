import math


def f11(x):
    d1 = ((x ** 2) + 45 * (x ** 3)) / (math.exp(x) + math.exp(x) + 90)
    d2 = ((30 * (x ** 7) + math.tan(x)) / (27 * (x ** 7) - math.fabs(x)))
    a = math.sqrt(10 * (x ** 5) - math.cos(x))
    return d1 - d2 + a
