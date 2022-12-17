class ListNode:
    def __init__(self, head) -> None:
        self.val = head
        self.next = None

    def add(self, value) -> None:
        cur = self
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(value)

    def append(self, value) -> None:
        self.add(value)

    def __repr__(self) -> str:
        if self.next is None:
            return f"({self.val})"
        repr = f"({self.val})"
        cur = self
        while cur.next is not None:
            cur = cur.next
            repr += f" -> ({cur.val})"
        return repr

    def reverse(self):
        # Check if single element
        if self.next is None:
            return self

        # Store elements in map
        idx = 1
        elements = {}
        elements[0] = self.val
        cur = self
        while cur.next is not None:
            cur = cur.next
            elements[idx] = cur.val
            idx += 1

        # Create reverse ListNode
        print(elements)
        idx -= 1
        reversedList = ListNode(elements[idx])
        idx -= 1

        # Add elements in reverse order
        while idx >= 0:
            reversedList.append(elements[idx])
            idx -= 1

        # Return reversed ListNode
        return reversedList


def main():
    l = ListNode(0)
    for i in range(1, 5):
        l.add(i)
    print(l)
    print(l.reverse())


if __name__ == "__main__":
    main()
