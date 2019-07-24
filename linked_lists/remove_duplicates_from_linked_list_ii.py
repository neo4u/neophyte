# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        dummy = ListNode(None)
        dummy.next = head

        prev_prev, prev, curr, duplicate = dummy, head, head.next, False

        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
                duplicate = True
            elif duplicate:
                prev_prev.next = prev.next
                prev = curr
                duplicate = False
            else:
                prev_prev = prev
                prev = curr
                duplicate = False

            curr = curr.next

        if duplicate:
            prev_prev.next = prev.next

        return dummy.next


class Solution2:
    def deleteDuplicates(self, head):
        dummy = pre = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next

        return dummy.next


# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# () -> 1  -> None
# pp    p      c