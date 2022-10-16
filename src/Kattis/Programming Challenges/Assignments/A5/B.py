for i in range(1, int(input()) + 1):
    size = int(input())
    v1 = sorted(list(map(int, input().split())))
    v2 = sorted(list(map(int, input().split())), reverse=True)
    s = 0
    for a, b in zip(v1, v2):
        s += a * b
    print(f"Case #{i}: {s}")
