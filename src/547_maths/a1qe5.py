# Name     : Zi Chen Hu
# McGill ID: 260931572


import math


# As per algorithm B.13 (Algorithm ModExp for efficient modular exponentiation)
# Input : Modulus N; base a in Z_N; integer exponent b > 0
# Output: [a^b mod N]
def exponent(a, b, N):
    x = a
    t = 1
    # Maintain the invariant that the answer is [t * x^b mod N]
    while b > 0:
        if b % 2 == 1:
            t = (t * x) % N
            b -= 1
        x = (x * x) % N
        b /= 2
    return t


N = 262915409
x = 123456789
print(exponent(x, 2, N))
print(exponent(202241377, 2, N))
print(202241377 % N)
print(987654321 * 65232893 - 1)
print(math.floor(64427548642780652 / 2))
