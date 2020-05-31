# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: return
        l1, l2 = self.split_list(head)
        l2 = self.reverse_list(l2)
        return self.merge_lists_alt(l1, l2)

    def split_list(self, head) -> bool:
        return head, self.find_split_point(head)

    def find_split_point(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None
        return mid

    def reverse_list(self, head) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def merge_lists_alt(self, l1, l2) -> ListNode:
        head = tmp = l1
        l1 = l1.next

        while l1 and l2:
            tmp.next = l2
            l2 = l2.next
            tmp = tmp.next

            tmp.next = l1
            l1 = l1.next
            tmp = tmp.next

        tmp.next = l1 or l2
        return head


# 143. Reorder List
# https://leetcode.com/problems/reorder-list/description/



# 1 -> 2 -> 3 -> 4 -> 5

#     s
#         f
# 1 2 3       4 5

#       s
#             f
# 1 2 3 4         5 6

# 1 6 2 5 3 4

# 1 -> 5 -> 2 -> 4 -> 3



# 1 2 3 4     5 6
#                 f
#       s

# 1 2 3 4    5 6 7
#                f
#       s

# Alternative merge with lesser lines but hard to understand
# Technique is to swap h1 and h2 at the end of iteration and
# keep performing the loop on h2
# def merge_lists(h1, h2)
#     head = tmp = h1
#     h1 = h1.next # Advance the first list as first node is in final place

#     while h2
#         tmp.next = h2
#         tmp = tmp.next
#         h2 = h2.next

#         h1, h2 = h2, h1 if h1
#     end

#     head
# end
