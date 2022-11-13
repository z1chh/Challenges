# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def n2(A):
    best = 2000000000
    for P in range(1, len(A)):
        cur = 0
        for el in A[:P]:
            cur += el
        for el in A[P:]:
            cur -= el
        if abs(cur) < best:
            best = abs(cur)
    return best

def solution(A):
    # write your code in Python 3.8.10
    return n2(A)
