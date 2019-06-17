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
