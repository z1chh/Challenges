qs, bc = map(int, input().split())
q = {}
pc = []
for i in range(qs):
    c, t = map(int, input().split())
    q.setdefault(t, []).append(c)
m = 0
for t in range(bc - 1, -1, -1):
    if t in q.keys():
        for c in q[t]:
            pc.append(c)
        if pc:
            m += max(pc)
            pc.remove(max(pc))
print(m)
