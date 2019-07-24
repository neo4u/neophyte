from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.boundary = [root.val]

        self.dfs_leftmost(root.left)
        self.dfs_leaves(root, root)
        self.dfs_rightmost(root.right)

        return self.boundary

    def dfs_leftmost(self, node):
        if not node or not node.left and not node.right: return
        self.boundary.append(node.val)

        if node.left:
            self.dfs_leftmost(node.left)
        else:
            self.dfs_leftmost(node.right)

    def dfs_leaves(self, root, node):
        if not node: return
        self.dfs_leaves(root, node.left)

        if node != root and not node.left and not node.right:
            self.boundary.append(node.val)

        self.dfs_leaves(root, node.right)

    def dfs_rightmost(self, node):
        if not node or not node.left and not node.right: return

        if node.right:
            self.dfs_rightmost(node.right)
        else:
            self.dfs_rightmost(node.left)

        self.boundary.append(node.val)


# 545. Boundary of Binary Tree
# https://leetcode.com/problems/boundary-of-binary-tree/description/
