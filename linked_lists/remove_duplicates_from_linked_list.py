# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        prv, cur = head, head.next

        while cur:
            if prv.val == cur.val:
                prv.next = cur.next
            else:
                prv = cur
            cur = cur.next

        return head


# Input:      [1,1,2,3,3]
# Output:     [1,2,3,3]
# Expected:   [1,2,3]