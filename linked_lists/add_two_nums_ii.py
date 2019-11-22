# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(None)
        s1, s2 = [], []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        while s1 or s2:
            v1, v2 = 0, 0

            if s1: v1 = s1.pop()
            if s2: v2 = s2.pop()

            carry, val = (v1 + v2 + carry).divmod(10)
            head.val = val
            temp = head

            head = ListNode(None)
            head.next = temp

        if carry: head.val = carry
        return head if head.val != -1 else head.next


# 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/description/
