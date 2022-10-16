import math


def eGCD(a, b):
    if a < b:
        d, X, Y = eGCD(b, a)
        return d, Y, X
    if a % b == 0:
        return (b, 0, 1)
    else:
        q = math.floor(a / b)
        r = a % b
        d, X, Y = eGCD(b, r)
        return (d, Y, X - Y * q)