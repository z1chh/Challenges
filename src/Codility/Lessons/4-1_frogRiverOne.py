# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.8.10
    s = set()
    time = -1
    for i in range(1, X + 1):
        s.add(i)
    while s:
        time += 1
        el = A[0]
        if el in s:
            s.remove(el)
        A.pop(0)
    return time
