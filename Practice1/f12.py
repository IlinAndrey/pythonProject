import math


def f12(x):
    if x < 68:
        res = x + 5 * (x ** 4)
        return '%.2e' % res
    elif x < 93:
        res = ((x ** 5) + 9 * (x ** 8))
        return '%.2e' % res
    elif x < 122:
        res = (((50 * (x ** 3)) - math.cos(x)) ** 8) - 23 * (x ** 6)
        return '%.2e' % res
    elif x < 154:
        res = 99 * ((math.tan(x) + math.tan(x) + 35) ** 6) + math.log(x)
        return '%.2e' % res
    else:
        res = (math.cos(x ** 6) - (x ** 8))
        return '%.2e' % res
