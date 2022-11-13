# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Get size of array
    size = len(A)
    
    # Base cases
    if size == 0:
        return 0
    elif size == 1:
        return A[0]
    elif size == 2:
        return abs(A[0] - A[1])
    elif size == 3:
        return abs(A[0] - A[1] - A[2])
    
    # Store sums from left and from right
    sumLeft = [A[0]]
    for i in range(size - 2):
        sumLeft.append(sumLeft[i] + A[i + 1])
    
    sumRight = [A[-1]]
    for i in range(size - 2):
        sumRight.append(sumRight[i] + A[-2 - i])
    
    # Get best split
    best = 2000000000
    for i in range(size - 1):
        if (cur := abs(sumLeft[i] - sumRight[-1 - i])) < best:
            best = cur
    return best
