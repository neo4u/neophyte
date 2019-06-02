# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root):
        inorder = []
        self.dfs(root, inorder)
        # self.dfs_iter(root, inorder)
        return inorder

    def dfs(self, root, inorder):
        if not root: return
        self.dfs(root.left, inorder)
        inorder.append(root.val)
        self.dfs(root.right, inorder)

    def dfs_iter(self, root, inorder):
        if not root: return
        stack, cur = [], root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            inorder.append(cur.val)
            cur = cur.right

        return inorder
