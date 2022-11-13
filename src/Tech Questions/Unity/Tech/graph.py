# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A, B):
    # write your code in Python 3.8.10
    # True if one single vertex
    if N == 1:
        return True
    
    vertices = set()
    
    # Iterate through both arrays -> O(n)
    for v1, v2 in zip(A, B):
        # If two consecutive vertices, add lowest to set
        if v2 == v1 + 1:
            vertices.add(v1)
        elif v1 == v2 + 1:
            vertices.add(v2)
    
    # Check if set contains vertices 1 to N -> O(n)
    for i in range(1, N):
        # Return False if one missing
        if i not in vertices:
            return False
    
    # Return True if set contains all vertices
    return True
