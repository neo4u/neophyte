# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} sum
# @return {Boolean}
def has_path_sum(root, sum)
	dfs(root, sum)
end

def dfs(root, sum)
	return false if root.nil?

	if is_leaf?(root)
		# Return true if the node is a leaf and the remaining sum if same a the value of the node
		root.val == sum
	else
		# Remove the value of non-leaf nodes from the target sum
		left = dfs(root.left, sum - root.val)
		right = dfs(root.right, sum - root.val)

		# Recursively check if the left or right sub-trees match the sum
		left || right
	end
end

def is_leaf?(node)
	node.left.nil? && node.right.nil?
end

# 112. Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# Note: A leaf is a node with no children.
# Example:
# Given the below binary tree and sum = 22,
#          5
#         / \
#        4   8
#       /   / \
#      11  13  4
#     /  \      \
#    7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# https://leetcode.com/submissions/detail/173323041/