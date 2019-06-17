# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal, head)
        if not head: return new_node

        node = head
        while True:
            # 1.A. Tipping point exists, and we've hit the peak and insert value is between max and min
            if node.next.val < node.val and (insertVal <= node.next.val or insertVal >= node.val):
                break
            # 1.B. Tipping point exists, and we're found a place for the insert value between the list
            elif node.val <= insertVal <= node.next.val:
                break
            # 2.   Tipping point doesn't exist, and we've hit the last node, before we loop back to start
            elif node.next == head:
                break

            node = node.next

        new_node.next = node.next
        node.next = new_node
        return head


# Approach 1: 3 Cases
# insert at the end;
# insert in the middle;
# insert before head (e.g. all the values are equal in the original list)


# Time: O(n)
# Space: O(1)


# 708. Insert into a Cyclic Sorted List
# https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/description/