# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Boolean}
def is_balanced(root)
  return true if root.nil?

  (get_height(root.left) - get_height(root.right)).abs <= 1 &&
  is_balanced(root.left) &&
  is_balanced(root.right)
end

def get_height(root)
  return 0 if root.nil?
  1 + [get_height(root.left), get_height(root.right)].max
end

# https://leetcode.com/problems/balanced-binary-tree/description/
# 110. Balanced Binary Tree
# Test on web site directly