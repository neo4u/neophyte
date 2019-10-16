from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = start = end = ListNode(0)
        dummy.next = head

        while end.next: # start stops at the last non-9 digit, end loops over all
            end = end.next
            if end.val != 9: start = end

        start.val += 1  # Plus One to start and set the rest 0
        while start.next:
            start = start.next
            start.val = 0

        return dummy if dummy.val == 1 else dummy.next


# 369. Plus One Linked List
# https://leetcode.com/problems/plus-one-linked-list/description/
