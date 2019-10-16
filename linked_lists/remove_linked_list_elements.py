# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val: head = head.next
        if not head or val is None: return

        prv, cur = head, head.next
        while cur:
            if cur.val == val:  prv.next = cur.next # If match is found, link prev node to next node
            else:               prv = cur           # If no match is found, link prev node to next node
            cur = cur.next

        return head


# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/


# Intuition:
# 1. We need to delete all nodes that have the same value as the given 'val'
# 2. We have only a reference to the head


# Steps:
# 1. First we need skip as manly 'val' nodes as possible
# 2. If we reach the end skipping 'val' nodes, then we return
# 