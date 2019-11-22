# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev, self.next = prev, next
        self.child = child


class Solution:
    def flatten(self, head):
        if not head: return
        prev = dummy = Node(0, None, head, None)
        stack = [head]

        while stack:
            node = stack.pop()

            node.prev = prev
            prev.next = node

            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None

            prev = node

        dummy.next.prev = None
        return dummy.next


# https://www.geeksforgeeks.org/amazon-interview-experience-set-189-for-sde1/


# 430. Flatten a Multilevel Doubly Linked List
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
