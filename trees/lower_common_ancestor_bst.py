# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Approach 1: Recursive
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        if not root or root == p or root == q: return root

        if p.val < root.val and q.val < root.val: return self.dfs(root.left, p, q)
        if p.val > root.val and q.val > root.val: return self.dfs(root.right, p, q)

        return root

# Approach 2: Iterative
# def lowest_common_ancestor(root, p, q)
#     while root
#         if p.val < root.val && q.val < root.val
#             root = root.left
#         elsif root.val < p.val && root.val < q.val
#             root = root.right
#         else
#             return root
#         end
#     end
# end


# Approach 1: Recursive
# Approach 2: Iterative