# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = curr = ListNode(None)

        while l1 or l2 or carry != 0:
            v1, v2 = 0, 0

            if l1: v1, l1 = l1.val, l1.next
            if l2: v2, l2 = l2.val, l2.next

            carry, val = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next


# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/
