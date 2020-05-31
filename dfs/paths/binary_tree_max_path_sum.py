# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = -float('inf')
        self.dfs(root)
        return self.max_sum

    def dfs(self, node: TreeNode) -> None:
        if not node: return 0

        l, r = self.dfs(node.left), self.dfs(node.right)
        self.max_sum = max(self.max_sum, l + node.val + r, l + node.val, r + node.val, node.val)

        return max(0, max(l, r) + node.val, node.val)


# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/


# Exactly 
# Intuition:
# Things to keep track of:
# 1. Node Sum: Maximum path sum ending at the current node (Returned from dfs)
# 2. Path Sum: Path sum for path including current node (Update max if this is greater)


left = TreeNode(2)
right = TreeNode(3)
root = TreeNode(1)
root.left, root.right = left, right
sol = Solution()
assert sol.maxPathSum(root) == 6

l2_left2, l2_right2 = TreeNode(15), TreeNode(7)
l1_left, l1_right = TreeNode(9), TreeNode(20)
l1_right.left, l1_right.right = l2_left2, l2_right2
root = TreeNode(-10)
root.left, root.right = l1_left, l1_right
assert sol.maxPathSum(root) == 42
