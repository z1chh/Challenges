# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(A, B):
    # write your code in Python 3.8.10
    # Total length must be at least 4
    if A + B < 4:
        return 0
    
    # Equal length
    if A == B:
        return math.floor(A / 2)
    
    # Avoid code duplication
    if A < B:
        return solution(B, A)
    
    # If A at leat 4 times as big as B
    if A / 4 >= B:
        return math.floor(A / 4)
    
    # Otherwise, check if it is better to split A in 3, or both in 2
    else:
        A_in_three = math.floor(A / 3)
        A_in_two = math.floor(A / 2)
        B_in_two = math.floor(B / 2)
        smallest = min(A_in_two, B_in_two)
        
        # In this case, we must cut each stick in two
        if A_in_three > B:
            return smallest
        else:
            # Otherwise, check which is better
            return max(A_in_three, smallest)
