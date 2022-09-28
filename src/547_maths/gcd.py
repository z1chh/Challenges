def GCD(a, N):
    if a < N:
        return GCD(N, a)
    if a % N == 0:
        return N
    else:
        return GCD(N, a % N)
