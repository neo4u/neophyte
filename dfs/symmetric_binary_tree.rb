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
def is_symmetric(root)
  !root || symmetric?(root.left, root.right)
end

def symmetric?(l, r)
  return symmetric?(l.left, r.right) && symmetric?(l.right, r.left) if l && r && l.val == r.val

  l == r
end

# require 'test/unit'
# extend Test::Unit::Assertions

# assert_equal(is_symmetric([1,2,2,3,4,4,3]), true)
# assert_equal(is_symmetric([1,2,2,null,3,null,3]), false)
# Tests won't work becuase the Tree needs to be constructed and I don't have that much patience. Test on leet code

# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/