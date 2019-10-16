# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal, None)
        if not head:
            new_node.next = new_node
            return new_node

        curr = head
        while True:
            # 1.A. Tipping point exists, and we've hit the peak and insert value is between max and min
            if curr.next.val < curr.val and (insertVal >= curr.val or insertVal <= curr.next.val):
                break
            # 1.B. Tipping point exists, and we're found a place for the insert value between the list
            elif curr.val <= insertVal <= curr.next.val:
                break
            # 2.   Tipping point doesn't exist, and we've hit the last node, before we loop back to start
            elif curr.next == head:
                break

            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node
        return head


# Approach 1: 3 Cases
# insert at the end;
# insert in the middle;
# insert before head (e.g. all the values are equal in the original list)


# Time: O(n)
# Space: O(1)


# 708. Insert into a Cyclic Sorted List
# https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/description/