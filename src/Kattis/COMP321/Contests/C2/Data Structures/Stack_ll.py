"""
STACK (FILO) - LINKEDLIST IMPLEMENTATION

Provides the following functions:
- is_empty() -> if the stack is empty
- pop()      -> Last in (throws ValueError if underflow)
- top()      -> Peek at the last in (throws ValueError if underflow)
- push()     -> Adds as first out
- len()      -> length
- str()      -> conversion to string

Notes:
- Initializes with a maximum size (list)
- Sorts its elements only when removing, peeking or casting to str
"""


class stack(object):
    class node(object):
        def __init__(self, value, link):
            self.value = value
            self.link = link

    def __init__(self):
        self.head = None

    def is_empty(self):  # could be __bool__()
        return self.head == None

    def push(self, value):
        self.head = stack.node(value, self.head)

    def top(self):
        if self.head == None:
            raise ValueError("Stack underflow")
        return self.head.value

    def pop(self):
        value = self.top()
        self.head = self.head.link
        return value

    def __len__(self):
        n = self.head
        if n is None:
            return 0
        tr = 1
        while n.link is not None:
            tr += 1
            n = n.link
        return tr

    def __repr__(self) -> str:
        n = self.head
        if n is None:
            return "[ ]"
        s = "[ "
        while n.link is not None:
            s += str(n.value) + " "
            n = n.link
        s += str(n.value) + " ]"
        return s


if __name__ == "__main__":
    print("Testing the linked list stack class.")
    import random

    def testn(N):
        st = stack()
        ls = random.sample(range(10000), N+1)
        for i in ls:
            st.push(i)

        assert st.top() == ls[-1]

        count = -1
        while not st.is_empty():
            assert st.pop() == ls[count]
            count -= 1

        # Force a stack underflow.
        try:
            st.pop()
        except ValueError as ex:
            assert str(ex) == "Stack underflow"
        else:
            assert False

# Matching brackets

    testn(1)
    testn(100)
    testn(3019)
    print("All tests passed.")

s = stack()
print(s)
s.push(10)
s.push(5)
s.push(10)
print(len(s))
print(s)
s.pop()
print(s)
print(len(s))