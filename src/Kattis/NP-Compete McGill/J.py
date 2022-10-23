size, s1, s2 = input().split()
size = int(size)
encountered = set()
d = {}
r = 0
s = 0
for c1, c2 in zip(s1, s2):
    if c1 == c2:
        r += 1
        if c1 in d:
            d[c1] += 1
        else:
            d[c1] = 1
for c1, c2 in zip(s1, s2):
    if c1 != c2:
        if c1 not in encountered and c1 in s2:
            encountered.add(c1)
            s += min(s1.count(c1), s2.count(c1))
            if c1 in d:
                s -= d[c1]
print(r, s)
