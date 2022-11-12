# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A, B):
    graph = {}
    for v1, v2 in zip(A, B):
        if v1 < v2:
            if v1 in graph:
                graph[v1].append(v2)
            else:
                graph[v1] = [v2]
        else:
            if v2 in graph:
                graph[v2].append(v1)
            else:
                graph[v2] = [v1]
    for i in range(1, N):
        if i not in graph:
            return False
        elif i + 1 not in graph[i]:
            return False
    return True
