# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root: return

        lvl_start = root
        while lvl_start:
            curr = lvl_start
            while curr:
                if curr.left: curr.left.next = curr.right
                if curr.right and curr.next: curr.right.next = curr.next.left
                curr = curr.next

            lvl_start = lvl_start.left

        return root