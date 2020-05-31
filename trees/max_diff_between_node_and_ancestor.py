# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max_diff = 0
        self.dfs(root, root.val, root.val)
        return self.max_diff

    def dfs(self, node: TreeNode, min_val: int, max_val: int):
        if not node: return

        # update maximal difference by max value and min value of ancestors
        self.max_diff = max(
            self.max_diff,
            abs(node.val - min_val),
            abs(node.val - max_val)
        )

        min_val = min(min_val, node.val)        # update min value of ancestors
        max_val = max(max_val, node.val)        # update max value of ancestors

        self.dfs(node.left, min_val, max_val)   # DFS on left sub-tree
        self.dfs(node.right, min_val, max_val)  # DFS on right sub-tree
