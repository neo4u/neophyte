"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return

        head, tail = self.dfs(root)
        head.left, tail.right = tail, head

        return head

    def dfs(self, root):
        l_head, l_tail, r_head, r_tail = root, root, root, root

        if root.left:
            l_head, l_tail = self.dfs(root.left)
            root.left = l_tail
            l_tail.right = root

        if root.right:
            r_head, r_tail = self.dfs(root.right)
            root.right = r_head
            r_head.left = root

        return l_head, r_tail