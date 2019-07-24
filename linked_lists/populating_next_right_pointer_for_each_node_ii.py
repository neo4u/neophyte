# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # curr:   The current node in the upper level
        # head_l: The left most node in the lower level
        # prev_l: The previous node in the lower level
        head_l, prev_l, curr = root, None, None

        while head_l:
            curr = head_l
            prev_l, head_l = None, None

            while curr:
                if curr.left:
                    if prev_l:
                        prev_l.next = curr.left
                    else:
                        head_l = curr.left
                    prev_l = curr.left

                if curr.right:
                    if prev_l:
                        prev_l.next = curr.right
                    else:
                        head_l = curr.right
                    prev_l = curr.right

                curr = curr.next

        return root


# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

# Time: O(n)
# Space: O(1)
