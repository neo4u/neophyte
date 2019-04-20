# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# Approach 1: DFS/Recursive
# @param {TreeNode} root
# @param {Float} target
# @return {Integer}
def closest_value(root, target)
    @closest = Float::INFINITY
    dfs(root, target)
    @closest
end

def dfs(node, trgt)
    return if !node
    
    @closest = node.val if (node.val - trgt).abs < (@closest - trgt).abs
    dfs(node.left, trgt) if trgt < node.val
    dfs(node.right, trgt) if trgt > node.val
end

# Approach 2: Iterative
# @param {TreeNode} root
# @param {Float} target
# @return {Integer}
def closest_value_iter(root, target)
    closest = root.val
    while root
        closest = root.val if (root.val - target).abs < (closest - target).abs
        root = target < root.val ? root.left : root.right
    end

    closest
end


# 270. Closest Binary Search Tree Value
# https://leetcode.com/problems/closest-binary-search-tree-value/description/

# Approach 1: Recurisve
# Time: O(n)
# Space: O(n)

# Approach 2: Iterative
# Time: O(n)
# Space: O(1)


require 'test/unit'
extend Test::Unit::Assertions

# Input: root = [4,2,5,1,3], target = 3.714286
#     4
#    / \
#   2   5
#  / \
# 1   3
root = TreeNode.new(4)
node2a, node2b = TreeNode.new(2), TreeNode.new(5)
root.left, root.right = node2a, node2b
node3a, node3b = TreeNode.new(1), TreeNode.new(3)
node2a.left, node2a.right = node3a, node3b

assert_equal(closest_value(root, 3.714286), 4)
assert_equal(closest_value_iter(root, 3.714286), 4)
