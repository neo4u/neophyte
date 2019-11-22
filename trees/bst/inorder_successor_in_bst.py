# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root: return

        if root.val <= p.val:
            # Greater elements are to the right
            return self.inorderSuccessor(root.right, p)
        else:
            # if root.val > p.val, then it'll be root itself or a node in the left sub-tree
            left = self.inorderSuccessor(root.left, p)
            return left if left else root


# 285. Inorder Successor in BST
# https://leetcode.com/problems/inorder-successor-in-bst/description/

# We need to find the node that has the smallest value > p.val


class Solution1:
    def inorderPredecessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root: return

        if root.val >= p.val:
            return self.inorderPredecessor(root.left, p)
        else:
            # entering this block means the current root is either p's parent or a node in p's right branch.
            right = self.inorderPredecessor(root.right, p)
            return right if right else root
