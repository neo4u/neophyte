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

        subtree_str = str(root.val)
        if root.left or root.right:
            l, r = self.convert(root.left), self.convert(root.right)

            subtree_str += "(" + l + ")"
            if r: subtree_str += "(" + r + ")"

        return subtree_str

# 4
#   (2(3)(1))
#   (6(5))