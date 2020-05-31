# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        if not root or root == p or root == q: return root

        l, r = self.dfs(root.left, p, q), self.dfs(root.right, p, q)
        if l and r: return root

        return l or r


# Approach 2: Iterative
# def lowest_common_ancestor(root, p, q)
#     stack = [root]
#     parent = { root => nil }

#     while !parent.key?(p) || !parent.key?(q)
#         node = stack.pop()
#         if node.left
#             parent[node.left] = node
#             stack.push(node.left)
#         end

#         if node.right
#             parent[node.right] = node
#             stack.push(node.right)
#         end
#     end

#     ancestors = Set.new()
#     while p
#         ancestors.add(p)
#         p = parent[p]
#     end

#     while !ancestors.include?(q)
#         q = parent[q]
#     end

#     q
# end

# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


# Approach 1: Recursive
# Approach 2: Iterative
