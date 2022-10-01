l = map(int, input().split())

d = {}

for el in l:
    if el in d.keys():
        d[el] += 1
    else:
        d[el] = 1

l = []
for val in d.values():
    l.append(val)

print(l)
