import math


def f11(x):
    d1 = ((x ** 2) + 45 * (x ** 3)) / (math.exp(x) + math.exp(x) + 90)
    d2 = ((30 * (x ** 7) + math.tan(x)) / (27 * (x ** 7) - math.fabs(x)))
    a = math.sqrt(10 * (x ** 5) - math.cos(x))
    res = d1 - d2 + a
    print('%.2e' % res)


f11(54)
f11(80)
