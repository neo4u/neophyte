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

# Faster solution: Keep checking for condition as we're calculating height
def is_balanced(root)
  dfs_height(root) != -1
end

def dfs_height(root)
  return 0 if root.nil?
  l = dfs_height(root.left)
  r = dfs_height(root.right)
  return -1 if l == -1          # left is balanced
  return -1 if r == -1          # right is balanced
  return -1 if (l - r).abs > 1  # height difference for left and right is at most 1

  1 + [l, r].max
end



# https://leetcode.com/problems/balanced-binary-tree/description/
# 110. Balanced Binary Tree
# Test on web site directly