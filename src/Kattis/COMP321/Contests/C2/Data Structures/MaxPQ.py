class MaxPQ:
    def __init__(self) -> None:
        self.queue = []
        self.size = 0
        self.ordered = True
    
    def add(self, value):
        self.queue.append(value)
        self.size += 1
        self.ordered = False
    
    def remove(self):
        if not self.ordered:
            self.queue.sort()
            self.ordered = True
        self.size -= 1
        return self.queue.pop()
    
    def top(self):
        if not self.ordered:
            self.queue.sort()
            self.ordered = True
        return self.queue[-1]
    
    def __len__(self):
        return self.size
    
    def __repr__(self) -> str:
        q = "[ "
        for el in self.queue:
            q += str(el) + " "
        q += "]"
        return q


if __name__ == "__main__":
    q = MaxPQ()
    print(q)
    q.add(9)
    q.add(6)
    q.add(5)
    q.add(3)
    q.add(94)
    print(q)
    print(q.remove())
    print(q)
