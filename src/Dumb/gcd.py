import math

def eGCD(a, b):
    if a % b == 0:
        return (b, 0, 1)
    else:
        q = math.floor(a / b)
        r = a % b
        d, X, Y = eGCD(b, r)
        return (d, Y, X - Y * q)

def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)
    
if __name__ == "__main__":
    print(eGCD(2, 1))
    print(eGCD(19, 7))
    print(eGCD(170, 25))
    print(GCD(2, 1))
    print(GCD(19, 7))
    print(GCD(170, 25))