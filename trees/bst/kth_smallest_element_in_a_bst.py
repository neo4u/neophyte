# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.kth_val = None
        self.k = k
        self.dfs(root)
        return self.kth_val

    def dfs(self, node):
        if not node: return

        self.dfs(node.left)

        self.k -= 1
        if self.k == 0:
            self.kth_val = node.val
            return

        self.dfs(node.right)


# root = [3,1,4,null,2], k = 1

# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/