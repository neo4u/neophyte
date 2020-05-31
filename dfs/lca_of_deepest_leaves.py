# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        _, lca = self.dfs(root)
        return lca

    def dfs(self, root: TreeNode):
        if not root: return 0, None
        l_ht, l = self.dfs(root.left)
        r_ht, r = self.dfs(root.right)

        if l_ht > r_ht: return l_ht + 1, l
        if r_ht > l_ht: return r_ht + 1, r

        return l_ht + 1, root



# 1123. Lowest Common Ancestor of Deepest Leaves
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/
