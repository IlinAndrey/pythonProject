import math


def f12(x):
    if x < 68:
        return x + 5 * (x ** 4)
    elif x < 93:
        return (x ** 5) + 9 * (x ** 8)
    elif x < 122:
        return (((50 * (x ** 3)) - math.cos(x)) ** 8) - 23 * (x ** 6)
    elif x < 154:
        return 99 * ((math.tan(x) + math.tan(x) + 35) ** 6) + math.log(x)
    else:
        return math.cos(x ** 6) - (x ** 8)