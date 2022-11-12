# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.8.10
    # Nothing to do if A empty
    size = len(A)
    if size == 0:
        return A
    
    # Simplify K
    if K >= size:
        K = K % size
    
    # Nothing to do if K == 0
    if K == 0:
        return A
    
    # Slice twice
    return A[-K:] + A[:size - K]

def main():
    print(solution([1, 2, 3, 4], 1))
    print(solution([1, 2, 3, 4], 2))
    print(solution([1, 2, 3, 4], 800))
    print(solution([1, 2, 3, 4], 109))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 111009))
    print(solution([], 1))

if __name__ == "__main__":
    main()