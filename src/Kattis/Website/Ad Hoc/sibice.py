import math


n, w, h = list(map(int, input().split()))
m = math.sqrt(w * w + h * h)
for _ in range(n):
    print("DA" if int(input()) <= m else "NE")
