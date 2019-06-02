# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        self.getDiameter(root)
        return self.ans - 1

    def getDiameter(self, node):
        if not node: return 0

        l, r = self.getDiameter(node.left), self.getDiameter(node.right)
        self.ans = max(self.ans, l + r + 1)
        return max(l, r) + 1
