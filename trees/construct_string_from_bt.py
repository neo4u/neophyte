# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        return self.dfs(t)

    def dfs(self, root):
        if not root: return ""

        result = str(root.val)
        if root.left or root.right:
            l, r = self.dfs(root.left), self.dfs(root.right)

            result += "(" + l + ")"
            if r: result += "(" + r + ")"

        return result

# 606. Construct String from Binary Tree
# https://leetcode.com/problems/construct-string-from-binary-tree/description/