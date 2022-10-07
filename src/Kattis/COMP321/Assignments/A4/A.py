n, bp = map(int, input().split())
b = list(map(lambda x: int(x) - bp, input().split()))
ms = b[0]
cs = 0
for i in range(n):
    cs += b[i]
    if cs > ms:
        ms = cs
    if cs < 0:
        cs = 0
print(ms)
