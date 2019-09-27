# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Approach 1: DFS/Recursive
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.closest = float('inf')
        self.dfs(root, target)
        return self.closest

    def dfs(self, node, trgt):
        if not node: return

        if abs(node.val - trgt) < abs(self.closest - trgt): self.closest = node.val
        if trgt == node.val: return

        if trgt < node.val: self.dfs(node.left, trgt)
        if trgt > node.val: self.dfs(node.right, trgt)


# Approach 2: Iterative
# @param {TreeNode} root
# @param {Float} target
# @return {Integer}
# def closest_value_iter(root, target)
#     closest = root.val
#     while root
#         closest = root.val if (root.val - target).abs < (closest - target).abs
#         root = target < root.val ? root.left : root.right
#     end

#     closest
# end


# 270. Closest Binary Search Tree Value
# https://leetcode.com/problems/closest-binary-search-tree-value/description/

# Approach 1: Recurisve

# Intuition:
# Since this is a BST,
# if target < curr_node.val, then everything in the right sub-tree will be further away, so look into the left sub-tree
# if target > curr_node.val, then everything in the left sub-tree will be further away, so look into the right sub-tree

# Time: O(n)
# Space: O(n)

# Approach 2: Iterative
# Time: O(n)
# Space: O(1)


# Input: root = [4,2,5,1,3], target = 3.714286
#     4
#    / \
#   2   5
#  / \
# 1   3

# root = TreeNode.new(4)
# node2a, node2b = TreeNode.new(2), TreeNode.new(5)
# root.left, root.right = node2a, node2b
# node3a, node3b = TreeNode.new(1), TreeNode.new(3)
# node2a.left, node2a.right = node3a, node3b

# assert_equal(closest_value(root, 3.714286), 4)
# assert_equal(closest_value_iter(root, 3.714286), 4)
