# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum_val: int) -> bool:
        return self.dfs(root, sum_val)

    def dfs(self, node, k):
        if not node: return False

        if self.is_leaf(node): return node.val == k
        else:
            diff = k - node.val
            l, r = self.dfs(node.left, diff), self.dfs(node.right, diff)
            return l or r

    def is_leaf(self, node):
        return not node.left and not node.right


# 112. Path Sum
# https://leetcode.com/problems/path-sum/description/


# Time: O(n)
# Space: Avg Case: O(log(n)), Worst Case: O(n)
