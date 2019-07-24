# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        self.lx, self.ly, self.px, self.py = -1, -2, None, None
        self.dfs(root, None, 0, x, y)
        return self.lx == self.ly and self.px != self.py

    def dfs(self, node, parent, level, x, y):
        if not node:
            return

        if node.val == x:
            self.lx = level
            self.px = parent

        if node.val == y:
            self.ly = level
            self.py = parent

        if self.px and self.py:
            return

        self.dfs(node.left, node, level + 1, x, y)
        self.dfs(node.right, node, level + 1, x, y)


# https://leetcode.com/problems/cousins-in-binary-tree/solution/
# 993. Cousins in Binary Tree
