class Solution:
    def minDepth(self, root: 'TreeNode') -> int:
        if not root: return 0
        _min, _max = sorted([self.minDepth(root.left), self.minDepth(root.right)])
        return 1 + (_min if _min > 0 else _max)


# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
