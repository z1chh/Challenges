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


def main():
    l = ListNode(0)
    for i in range(1, 5):
        l.add(i)
    print(l)


if __name__ == "__main__":
    main()