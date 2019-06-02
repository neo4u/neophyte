# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, l: int=-float('inf'), r: int=float('inf')) -> bool:
        if not root: return True
        if not l <= root.val <= r: return False

        return isValidBST(root.left, l, root.val - 1) and isValidBST(root.right, root.val + 1, r)