# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode, _min=float('-inf'), _max=float('inf')) -> bool:
        if not root: return True
        val = root.val
        if not _min <= val <= _max: return False

        return self.isValidBST(root.left, _min, val - 1) and self.isValidBST(root.right, val + 1, _max)



# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/
