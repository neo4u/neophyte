class Solution:
    def countNodes(self, root):
        if not root: return 0
        l_depth = self.dfs_left(root.left)
        r_depth = self.dfs_left(root.right)

        if l_depth == r_depth:
            return pow(2, l_depth) - 1 + 1 + self.countNodes(root.right)
        else:
            return pow(2, r_depth) - 1 + 1 + self.countNodes(root.left)

    def dfs_left(self, root):
        if not root: return 0
        return 1 + self.dfs_left(root.left)


# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/description/
