# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre or not post: return
        root = TreeNode(pre[0])
        if len(post) == 1: return root

        i = pre.index(post[-2])
        root.left = self.constructFromPrePost(pre[1:i], post[:i - 1])
        root.right = self.constructFromPrePost(pre[i:], post[i - 1:-1])

        return root


# 889. Construct Binary Tree from Preorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
