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


def GCD(a, b):
    if a < b:
        return GCD(b, a)
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)


def inverse(a, N):
    d, X, Y = eGCD(a, N)
    if d == 1:
        return X % N
    else:
        raise Exception("Error: no inverse")


def exponent(a, b, N):
    x = a
    t = 1
    while b > 0:
        if b % 2 == 1:
            t = (t * x) % N
            b -= 1
        x = (x * x) % N
        b /= 2
    return t

if __name__ == "__main__":
    def geteGCD(a, b):
        print("eGCD({a}, {b}) = {x}".format(a = a, b = b, x = eGCD(a, b)))

    def getGCD(a, b):
        print("GCD({a}, {b}) = {x}".format(a = a, b = b, x = GCD(a, b)))

    def getInverse(a, N):
        print("[{a}^(-1) mod {N}] = {x}".format(a = a, N = N, x = inverse(a, N)))
        
    def getExp(a, b, N):
        print("[{a}^{b} mod {N}] = {x}".format(a = a, b = b, N = N, x = exponent(a, b, N)))

    geteGCD(2, 1)
    geteGCD(7, 19)
    geteGCD(19, 7)
    geteGCD(170, 25)

    getGCD(2, 1)
    getGCD(19, 7)
    getGCD(170, 25)

    getInverse(19, 7)
    getInverse(7, 19)
    
    getExp(5, 13, 7)
