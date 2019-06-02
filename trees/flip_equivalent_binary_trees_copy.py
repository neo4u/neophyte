# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flipEquiv(self, t1, t2):
        if not t1 and not t2:
            return True
        if bool(t1) != bool(t2):
            return False
        if t1.val != t2.val:
            return False

        l1, l2, r1, r2 = t1.left, t2.left, t1.right, t2.right
        return (self.flipEquiv(l1, l2) and self.flipEquiv(r1, r2) or
                self.flipEquiv(l1, r2) and self.flipEquiv(r1, l2))


class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))