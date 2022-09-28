def GCD(a, b):
    if a < b:
        return GCD(b, a)
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)
