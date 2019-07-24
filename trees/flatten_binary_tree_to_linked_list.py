# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: return None

        tmp_l, tmp_r = root.left, root.right
        self.flatten(root.left)
        self.flatten(root.right)

        if not tmp_l: return

        root.right = tmp_l
        root.left = None

        while tmp_l.right: tmp_l = tmp_l.right
        tmp_l.right = tmp_r

# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


# This solution is adapted from this Java solution.
# You basically maintain a global variable prev which stores the last node that was flattened.
# First you flatten root.right, after which prev is root.right.
# Then you flatten root.left, which gets called recursively until you hit the 'end',
# at which point the flattened root.right is attached to the right of the 'end',
# and finally prev gets set to root.left. After the recursive calls,
# root.right get set to root.left, which already has the root.right attached to its end.
