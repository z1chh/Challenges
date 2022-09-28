from exponent import *
from qr import *


def sqrt(p, a):
    qr, qnr = quadratic_residues()  # ADD PARAMS
    b = qnr[0]
    r = (p - 1) / 2
    r2 = 0

    while r % 2 == 0:
        r /= 2
        r2 /= 2
        ans1 = exponent(a, r, p)
        ans2 = exponent(b, r2, p)
        ans = (ans1 * ans2) % p
        if ans == p - 1:
            r2 += (p - 1) / 2

    ans1 = exponent(a, (r + 1) / 2, p)
    ans2 = exponent(b, r2 / 2, p)
    return (ans1 * ans2) % p
