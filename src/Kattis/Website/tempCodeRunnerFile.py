n, w, h = list(map(int, input().split()))
m = w if w > h else h
for _ in range(n):
    print("DA" if int(input()) <= m else "NE")
