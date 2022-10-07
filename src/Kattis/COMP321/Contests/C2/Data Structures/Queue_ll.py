"""
QUEUE (FIFO) - LINKEDLIST IMPLEMENTATION

Provides the following functions:
- is_empty() -> if the stack is empty
- dequeue()  -> First in (throws ValueError if underflow)
- top()      -> Peek at the first in (throws ValueError if underflow)
- enqueue()  -> Adds to queue
- len()      -> length
- str()      -> conversion to string

Notes:
- Initializes as empty queue
- Sorts its elements only when removing, peeking or casting to str
"""


class queue:
    class node:
        def __init__(self, value, link=None):
            self.value = value
            self.link = link

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        newnode = queue.node(value)
        if self.tail != None:
            self.tail.link = newnode
        self.tail = newnode
        if self.head == None:
            self.head = newnode

    def dequeue(self):
        if not self.head:
            raise ValueError("Queue underflow")
        result = self.head.value
        self.head = self.head.link
        return result

    def top(self):
        if not self.head:
            raise ValueError("Queue underflow")
        return self.head.value

    def __len__(self):
        n = self.head
        if n is None:
            return 0
        tr = 1
        while n.link is not None:
            tr += 1
            n = n.link
        return tr

    def __str__(self):
        result = '['
        node = self.head
        while node != None:
            result += str(node.value)
            if node.link != None:
                result += ", "
            node = node.link
        result += ']'
        return result

# waiting list


if __name__ == "__main__":
    q = queue()
    for i in range(10):
        q.enqueue(i)
    print(q)
    i = q.dequeue()
    q.enqueue(i)
    print(q)
    for i in range(10):
        print(q.dequeue())
    print(q)
    q.enqueue(100)
    q.enqueue(101)
    print(q.dequeue())
    print(q)
