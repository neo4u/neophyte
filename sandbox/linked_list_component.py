# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count, started = 0, False
        G = set(G)

        while head:
            if head.val in G:
                if not started:
                    started = True
                    count += 1
            else:
                started = False
            head = head.next

        return count
