a, b, c = map(int, input().split())
tot = a + b
tr = 0
while tot >= c:
    tot -= (c - 1)
    tr += 1
print(tr)
