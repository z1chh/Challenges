# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(A, B):
    # write your code in Python 3.8.10
    # Check if long enough to create 4 sticks
    if A + B < 4:
        return 0
    
    # Code
    if A == B:
        return math.floor(A / 2)
    elif A > B:
        if A / 4 > B:
            return math.floor(A / 4)
        else:
            t = math.floor(A / 3)
            d = min(math.floor(A / 2), math.floor(B / 2))
            if t <= B:
                return max(t, d)
            else:
                return d
    else:
        return solution(B, A)