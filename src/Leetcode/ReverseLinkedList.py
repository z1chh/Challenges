# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Check if single element
        if head is None:
            return None
        if head.next is None:
            return ListNode(head.val)

        # Store elements in map
        idx = 1
        elements = {}
        elements[0] = head.val
        cur = head
        while cur.next is not None:
            cur = cur.next
            elements[idx] = cur.val
            idx += 1

        # Create reverse ListNode
        idx -= 1
        reversedList = ListNode(elements[idx])
        idx -= 1

        # Add elements in reverse order
        cur = reversedList
        while idx >= 0:
            cur.next = ListNode(elements[idx])
            cur = cur.next
            idx -= 1

        # Return reversed ListNode
        return reversedList
