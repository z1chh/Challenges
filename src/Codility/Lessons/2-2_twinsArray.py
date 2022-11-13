# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
    if not A:
        return 0
    s = set()
    for el in A:
        if el in s:
            s.remove(el)
        else:
            s.add(el)
    for el in s:
        return el

