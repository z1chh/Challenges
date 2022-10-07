"""
MAX PRIORITY QUEUE

Provides the following functions:
- add(value) -> Add value to MaxPQ
- remove()   -> Max P
- top()      -> Peek at the Max P
- len()      -> length
- str()      -> conversion to string

Notes:
- Initializes as empty MaxPQ
- Sorts its elements only when removing, peeking or casting to str
"""


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
        if not self.ordered:
            self.queue.sort()
            self.ordered = True
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
