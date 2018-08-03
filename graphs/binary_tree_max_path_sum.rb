# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# @param {TreeNode} root
# @return {Integer}
def max_path_sum(root)
  @max = -Float::INFINITY
  max_path(root)

  @max
end

def max_path(root)
  return 0 if root.nil?
  left, right = max_path(root.left), max_path(root.right)
  path_sum = root.val + left + right
  @max = path_sum if path_sum > @max

  [[left, right].max + root.val, 0].max
end

# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

require 'test/unit'
extend Test::Unit::Assertions

left = TreeNode.new(2)
right = TreeNode.new(3)
root = TreeNode.new(1)
root.left, root.right = left, right 
assert_equal(max_path_sum(root), 6)

l2_left2, l2_right2 = TreeNode.new(15), TreeNode.new(7)
l1_left, l1_right = TreeNode.new(9), TreeNode.new(20)
l1_right.left, l1_right.right = l2_left2, l2_right2
root = TreeNode.new(-10)
root.left, root.right = l1_left, l1_right
assert_equal(max_path_sum(root), 42)
