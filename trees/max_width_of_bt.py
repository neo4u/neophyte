# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        q, max_width = [(root, 0, 0)], 1

        while q:
            level_q = []
            for node, depth, pos in q:
                if node.left: level_q.append((node.left, depth + 1, 2 * pos))
                if node.right: level_q.append((node.right, depth + 1, 2 * pos + 1))

            if level_q:
                max_width = max(max_width, level_q[-1][2] - level_q[0][2] + 1)
            q = level_q

        return max_width


# https://leetcode.com/problems/maximum-width-of-binary-tree/
# 662. Maximum Width of Binary Tree