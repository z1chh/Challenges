w, p = map(int, input().split())
o = list(map(int, input().split()))
o.append(0)
o.append(w)
tr = set()
tr.add(w)
for i in range(p + 1):
    for j in range(i + 1, p + 2):
        tr.add(abs(o[i] - o[j]))
tr = map(str, sorted(list(tr)))
print(" ".join(tr))
