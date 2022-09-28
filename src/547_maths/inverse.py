from eGCD import *


def inverse(a, N):
    d, X, Y = eGCD(a, N)
    if d == 1:
        return X % N
    else:
        raise Exception("Error: no inverse")
