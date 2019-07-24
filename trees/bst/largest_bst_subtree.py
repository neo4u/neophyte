# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.max_size = 0

    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_size

    def dfs(self, node):
        if not node: return 0, 0, 0

        l_size, l_min, l_max = self.dfs(node.left)
        r_size, r_min, r_max = self.dfs(node.right)

        if (l_size == 0 or l_size > 0 and node.val > l_max) and (r_size == 0 or r_size > 0 and node.val < r_min):
            size = 1 + l_size + r_size
            self.max_size = max(self.max_size, size)
            node_min = node.val if l_size == 0 else l_min
            node_max = node.val if r_size == 0 else r_max
            return size, node_min, node_max

        return -1, 0, 0
