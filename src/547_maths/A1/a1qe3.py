# Name     : Zi Chen Hu
# McGill ID: 260931572

from matplotlib import pyplot as plt


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
x = 260931572
bitmap = [[0] * 256 for i in range(256)]
for i in range(256):
    for j in range(256):
        bitmap[i][j] = x % 2
        x = exponent(x, 2, N)
plt.imshow(bitmap, interpolation="nearest")
plt.show()
