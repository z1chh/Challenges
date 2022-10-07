"""
QUEUE (FIFO) - ARRAY IMPLEMENTATION

Provides the following functions:
- is_empty() -> if the stack is empty
- dequeue()  -> First in (throws ValueError if underflow)
- top()      -> Peek at the first in (throws ValueError if underflow)
- enqueue()  -> Adds to queue
- len()      -> length
- str()      -> conversion to string

Notes:
- Initializes as empty queue
"""


class queue(object):
    '''A very simple, fixed-capacity, queue class.'''

    def __init__(self, capacity=10):
        '''Initialize the stack to a fixed capacity.'''
        self.data = [0] * capacity
        self.head = self.tail = 0
        self.size = capacity
        self.used = 0

    def is_empty(self):
        '''Return True if the queue is empty.'''
        return self.used == 0

    def enqueue(self, value):
        '''Add a value to the tail of the queue.'''
        if self.used >= self.size:
            raise ValueError("Queue overflow")
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.used += 1

    def peek(self):
        '''Return the value at the head of the queue.'''
        if self.is_empty():
            raise ValueError("Queue underflow")
        return self.data[self.head]

    def dequeue(self):
        '''Remove a value from the head of the queue.'''
        result = self.peek()
        self.data[self.head] = None  # Clear location (avoid loitering).
        self.head = (self.head + 1) % self.size
        self.used -= 1
        return result

    def __len__(self):
        return self.used

    def __repr__(self) -> str:
        s = "[ "
        ind = self.head
        for i in range(self.used):
            s += str(self.data[ind + i]) + " "
        s += "]"
        return s


if __name__ == "__main__":
    import random
    print("Testing the simple queue class.")

    def testn(N):
        qu = queue(N+1)
        ls = random.sample(range(10000), N+1)
        for i in ls:
            qu.enqueue(i)

        assert qu.peek() == ls[0]

        count = 0
        while not qu.is_empty():
            assert qu.dequeue() == ls[count]
            count += 1

        # Force a queue underflow.
        try:
            qu.dequeue()
        except ValueError as ex:
            assert str(ex) == "Queue underflow"
        else:
            assert False

        # Force a queue overflow:
        try:
            for i in range(N+2):
                qu.enqueue(i)
        except ValueError as ex:
            assert str(ex) == "Queue overflow"
        else:
            assert False

        assert qu.dequeue() == 0
        assert qu.dequeue() == 1
    testn(1)
    testn(100)
    testn(3019)
    print("All tests passed.")
