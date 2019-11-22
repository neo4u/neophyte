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

        i = pre.index(post[-2]) # get index of value that starts the right sub-tree
        # pre is from 1 to i - 1, cuz we leave 0 as it is root, and stop before i cuz that's the start of right sub-tree
        # post is from 0 to i - 2, cuz we know that i is the index of right sub-tree start in pre, so we can guess that i - 1 will be the end index for left-subtree in post, cuz -1 for root
        root.left = self.constructFromPrePost(pre[1:i], post[:i - 1])

        # pre is from i to n - 1, cuz that's start of right sub-tree, and post i - 1, n - 2, i - 1, is start of right portion of array
        root.right = self.constructFromPrePost(pre[i:], post[i - 1:-1])

        return root


# 889. Construct Binary Tree from Preorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
