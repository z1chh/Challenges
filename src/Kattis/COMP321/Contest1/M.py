c, s = list(map(int, input().split()))
cp = 0
possible = True
for _ in range(s):
    l, e, n = list(map(int, input().split()))
    cp -= l
    if not possible:
        continue
    if cp < 0:
        possible = False
    cp += e
    if cp > c:
        possible = False
    if cp < c and n > 0:
        possible = False

if cp != 0:
    possible = False
print("possible" if possible else "impossible")
