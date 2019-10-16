# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Iterative
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = cur = ListNode(-1)
        dummy.next = head

        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next

            cur.next = second
            first.next = second.next
            second.next = first

            cur = cur.next.next

        return dummy.next


# Recursive
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            nxt = head.next
            head.next = self.swapPairs(nxt.next)
            nxt.next = head
            return nxt

        return head
