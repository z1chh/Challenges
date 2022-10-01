# Greedy
nc = int(input())
for i in range(1, nc + 1):
    size = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    v1.sort()
    v2.sort()
    v2.reverse()
    s = 0
    for a, b in zip(v1, v2):
        s += a * b
    print(s)
