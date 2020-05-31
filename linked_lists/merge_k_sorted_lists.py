from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Approach 5: Divide and Conquer (Merge Sort Way)
class Solution:
    def mergeKLists(self, lists: List[ListNode], ) -> ListNode:
        if not lists: return
        return self.merge_k_lists(lists, 0, len(lists) - 1)

    def merge_k_lists(self, lists, s, e):
        if s == e: return lists[s]

        mid = (s + e) // 2
        l1, l2 = self.merge_k_lists(lists, s, mid), self.merge_k_lists(lists, mid + 1, e)
        return self.merge_2_lists(l1, l2)

    def merge_2_lists(self, l1, l2):
        dummy = curr = ListNode(None)

        while l1 or l2:
            if l1 and l2 and l1.val < l2.val or not l2:
                curr.next, l1 = l1, l1.next
            elif l1 and l2 or not l1:
                curr.next, l2 = l2, l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next


# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/

# There are 5 approaches
# Approach 1: Brute force, collect all nodes and sort by value. Approach from above.
# Time: O(nlog(n))
# Space: O(n)

# Approach 2: Iterate through all the lists and take the minimum from the k lists 
# Time: O(k * n)
# Space: O(1)

# Approach 3: The comparison process can be optimized in the above process using priority queue.
# Time: O(nlogk)
# Space: O(1)

# Approach 4: Divide and Conquer, Merge k lists k-1 times two at a time.
# Time: O(nk)
# Space: O(1)

# Approach 5: Divide and Conquer, Merge sort way (Optimal)
# Time: O(nlogk)
# Space: O(log(k)), log(k) for stack

# Approach 6: Divide and Conquer, Iterative
# Time: O(nlogk)
# Space: O(1)
