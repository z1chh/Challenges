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

def better(A):
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
    for i in range(size - 1):
        sumLeft.append(sumLeft[i] + A[i + 1])
    
    sumRight = [A[-1]]
    for i in range(size - 1):
        sumRight.append(sumRight[i] + A[-2 - i])
    
    # Get best split
    best = 2000000000
    for i in range(size - 1):
        if abs(sumLeft[i] - sumRight[-2 - i]) < best:
            best = abs(sumLeft[i] - sumRight[-2 - i])
    return best

def solution(A):
    # write your code in Python 3.8.10
    return better(A)

def main():
    print(solution([3, 1, 2, 4, 3]))

if __name__ == "__main__":
    main()