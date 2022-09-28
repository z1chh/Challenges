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
