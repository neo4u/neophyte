# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Approach 1: Recursion
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Approach 2: Itervative (Optimal)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(None)

        while l1 or l2:
            if l1 and l2 and l1.val < l2.val or not l2:
                curr.next, l1 = l1, l1.next
            elif l1 and l2 or not l1:
                curr.next, l2 = l2, l2.next

            curr = curr.next

        return dummy.next


# Approach 1: Recursion
# Time: O(n + m)
# Space: O(n + m)

# Approach 2: Iteravtive
# Time: O(n + m)
# Space: O(1)
