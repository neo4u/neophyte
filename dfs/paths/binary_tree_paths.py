# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        self.dfs(root)
        return self.paths

    def dfs(self, root, path=[]):
        if not root: return
        path = path + [str(root.val)]

        if not root.left and not root.right:
            self.paths.append("->".join(path))
        else:
            self.dfs(root.left, path)
            self.dfs(root.right, path)


# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/

# Time: O(n)
# Space: Avg O(log(n)), Worst case O(n), Based on the depth of the tree for call stack.