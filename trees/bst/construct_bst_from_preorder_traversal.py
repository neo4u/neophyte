# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder, vmin=-float('inf'), vmax=float('inf')):
        if not preorder: return

        val = preorder[0]
        if not vmin <= val <= vmax: return
        preorder.pop(0)

        root = TreeNode(val)
        root.left = self.bstFromPreorder(preorder, vmin, val - 1)
        root.right = self.bstFromPreorder(preorder, val + 1, vmax)

        return root


# 1008. Construct Binary Search Tree from Preorder Traversal
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
