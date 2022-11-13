# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
    for idx, val in enumerate(sorted(A)):
        if idx + 1 != val:
            return idx + 1
    return len(A) + 1
