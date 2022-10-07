"""
STACK (FILO) - ARRAY IMPLEMENTATION

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
    def __init__(self, capacity=10):
        self.data = [0] * capacity
        self.sp = -1            # Stack pointer

    def is_empty(self): return self.sp < 0

    def top(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        return self.data[self.sp]

    def push(self, value):
        if self.sp + 1 == len(self.data):
            raise ValueError("Stack overflow")
        self.sp += 1            # Increment pointer.
        self.data[self.sp] = value

    def pop(self):
        result = self.top()
        self.data[self.sp] = None  # Avoid loitering.
        self.sp -= 1            # Decrement pointer.
        return result

    def __len__(self):
        return self.sp + 1

    def __repr__(self) -> str:
        s = "[ "
        for i in range(self.sp + 1):
            s += str(self.data[i]) + " "
        s += "]"
        return s


if __name__ == "__main__":
    print("Testing the simple stack class.")
    import random

    def testn(N):
        st = stack(N+1)
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

        # Force a stack overflow:
        try:
            for i in range(N+2):
                st.push(i)
        except ValueError as ex:
            assert str(ex) == "Stack overflow"
        else:
            assert False

        assert st.pop() == N
        assert st.pop() == N-1
    testn(1)
    testn(100)
    testn(3019)
    print("All tests passed.")
