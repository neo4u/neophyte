# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        tmp = head
        seen = {}
        while tmp:
            if id(tmp) in seen:
                return True
            else:
                seen[id(tmp)] = 1
                tmp = tmp.next
        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: return True

        return False


# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/
