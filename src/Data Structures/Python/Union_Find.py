class UF:
    def __init__(self) -> None:
        self.p = dict()

    def find(self, val):
        if v := self.p[val] == val:
            return val
        else:
            return self.find(v)

    def union(self, v1, v2):
        self.p[self.find(v1)] = v2

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
                self.p[v1] = v1
                self.p[v2] = v1
