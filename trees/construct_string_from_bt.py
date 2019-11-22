# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        return self.dfs(t)

    def dfs(self, node):
        if not node: return ''

        result = str(node.val)
        if node.left or node.right:
            l, r = self.dfs(node.left), self.dfs(node.right)
            result += f"({l})"
            if r: result += f"({r})"

        return result


# 606. Construct String from Binary Tree
# https://leetcode.com/problems/construct-string-from-binary-tree/description/