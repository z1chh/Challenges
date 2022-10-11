class UF:
    def __init__(self) -> None:
        self.p = dict()
        self.p[1] = 1

    def find(self, val):
        v = self.p[val]
        if v == val:
            return val
        else:
            return self.find(v)

    def update(self, val, repr):
        v_repr = self.p[val]
        if val == v_repr:
            self.p[val] = repr
        elif v_repr != repr:
            self.p[val] = repr
            self.update(v_repr, repr)
        else:
            self.p[val] = repr

    def union(self, v1, v2, f1, f2):
        if (f1 == 1):
            self.update(v1, f2)
        else:
            self.update(v2, f1)

    def add(self, v1, v2):
        if v1 in self.p:
            f1 = self.find(v1)
            if v2 in self.p:
                f2 = self.find(v2)
                if f1 != f2:
                    self.union(v1, v2, f1, f2)
            else:
                self.p[v2] = f1
        else:
            if v2 in self.p:
                f2 = self.find(v2)
                self.p[v1] = f2
            else:
                if v1 == 1:
                    self.p[v1] = v1
                    self.p[v2] = v1
                else:
                    self.p[v1] = v2
                    self.p[v2] = v2


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
