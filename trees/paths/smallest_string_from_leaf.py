# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode, current: str = "") -> str:
        vals = "abcdefghijklmnopqrstuvwxyz{}"
        current = vals[root.val] + current
        if not root.left and not root.right:
            return current
        if root.left and root.right:
            l = self.smallestFromLeaf(root.left, current)
            r = self.smallestFromLeaf(root.right, current)
            return l if l < r else r

        if root.right: return self.smallestFromLeaf(root.right, current)
        if root.left: return self.smallestFromLeaf(root.left, current)


# 988. Smallest String Starting From Leaf
