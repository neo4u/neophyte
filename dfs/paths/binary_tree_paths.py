from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        self.dfs(root, [])
        return self.paths

    def dfs(self, root, path):
        if not root: return
        path = path + [str(root.val)]

        if self.is_leaf(root):  self.paths.append("->".join(path))
        else:                   self.dfs(root.left, path); self.dfs(root.right, path)

    def is_leaf(self, node):
        return not node.left and node.right



# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/

# Intuition:
# - Again here only paths from root to leaf are considered and not root to None nodes
#   So we need to explicitly check for leaf nodes as the terminating conditions
# - Same like min depth of binary tree and 112. Path Sum

# Time: O(n)
# Space: Avg O(log(n)), Worst case O(n), Based on the depth of the tree for call stack.
