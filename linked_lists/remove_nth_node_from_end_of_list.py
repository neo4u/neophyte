# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = slow = fast = ListNode(None)
        dummy.next = head

        for _ in range(n + 1): fast = fast.next
        while fast: slow, fast = slow.next, fast.next
        slow.next = slow.next.next

        return dummy.next



# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Approach 1: Two pass

# Aprroach 2: One Pass
# Steps:
# 1. We use two pointers slow and fast
# 2. We also use a dummy pointer before head and set slow and fast to dummy which is 1 node before head
# 3. We iterate n + 1 times and advance fast
# 4. So fast is n nodes ahead of slow
# 5. Now we advance slow and fast until fast hits the end
# 6. At this point slow is pointing to the nth node from the end
# 7. We swap slow.next and slow.next.next
# 8. We return the dummy.next pointing to the head

# Time: O(n),
# Space : O(1)


# ()->1 ->  2 ->  3 ->  4 -> 5
