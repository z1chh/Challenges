from GCD import *
from exponent import *

def sqrt(p, a):
    r = (p - 1) / 2
    r2 = 0
    
    while r % 2 == 0:
        r /= 2
        r2 /= 2
        ans1 = exponent(a, r, p)
        ans2 = exponent(b, r2, p)
        ans = GCD(ans1 * ans2, p)
    return -1