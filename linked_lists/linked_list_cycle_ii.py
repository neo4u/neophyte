# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else:
            return None

        while slow != head: slow, head = slow.next, head.next
        return head


# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/description/
