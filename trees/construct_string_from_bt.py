# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        return self.convert(t)

    def convert(self, root):
        if not root: return ""

        result = str(root.val)
        if root.left or root.right:
            l, r = self.convert(root.left), self.convert(root.right)

            result += "(" + l + ")"
            if r: result += "(" + r + ")"

        return result
