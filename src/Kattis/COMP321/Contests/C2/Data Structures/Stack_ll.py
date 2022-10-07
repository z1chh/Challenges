class stack(object):
    class node(object):
        def __init__(self, value, link):
            self.value = value
            self.link = link
    def __init__(self):
        self.head = None
    def isEmpty(self): # could be __bool__()
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
        while not st.isEmpty():
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
