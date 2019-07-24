# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.max_size = 0
        self.dfs(root)
        return self.max_size

    def dfs(self, root):
        if not root: return 0, 0, 0

        l_size, l_min, l_max = self.dfs(root.left)
        r_size, r_min, r_max = self.dfs(root.right)

        if (l_size == 0 or l_size > 0 and root.val > l_max) and (r_size == 0 or r_size > 0 and root.val < r_min):
            size = l_size + r_size + 1
            self.max_size = max(self.max_size, size)

            node_min = root.val if l_size == 0 else l_min
            node_max = root.val if r_size == 0 else r_max

            return size, node_min, node_max

        return -1, 0, 0
