# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder: return
        root_val = postorder.pop()

        root = TreeNode(root_val)
        i = inorder.index(root_val)
        root.right = self.buildTree(inorder[i + 1:], postorder)
        root.left = self.buildTree(inorder[:i], postorder)
        return root


# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
