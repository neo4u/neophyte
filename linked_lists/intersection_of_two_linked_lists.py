# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None: return None
        a_ptr, b_ptr = headA, headB

        while a_ptr != b_ptr:
            a_ptr = headB if not a_ptr else a_ptr.next
            b_ptr = headA if not b_ptr else b_ptr.next

        return a_ptr
