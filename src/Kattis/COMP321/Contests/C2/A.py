class UF:
    def __init__(self) -> None:
        self.p = dict()

    def find(self, val):
        def _find(d, val):
            if val not in d:
                raise ValueError("DNE")
            if d[val] == val:
                return val
            else:
                return _find(d, d[val])
        return _find(self.p, val)

    def union(self, v1, v2):
        if self.find(v1) != self.find(v2):
            self.p[self.find(v2)] = self.find(v1)

    def add(self, v1, v2):
        if v1 in self.p:
            if v2 in self.p:
                if self.find(v1) != self.find(v2):
                    self.union(v1, v2)
            else:
                self.p[v2] = v1
        else:
            if v2 in self.p:
                self.p[v1] = v2
            else:
                self.p[v1] = v1
                self.p[v2] = v1

uf = UF()
nh, c = map(int, input().split())
allh = set()
allh.add(1)
for _ in range(c):
    a, b = map(int, input().split())
    allh.add(a)
    allh.add(b)
    if b == 1:
        uf.add(b, a)
    else:
        uf.add(a, b)
ni = set()
for h in uf.p:
    if uf.find(h) != 1:
        ni.add(h)
for i in range(1, nh + 1):
    if i not in allh:
        ni.add(i)
if len(ni) == 0:
    print("Connected")
else:
    for h in sorted(ni):
        print(h)
