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
def is_valid_bst(root, l = nil, r = nil)
  return true if root.nil?

  return false if l && l > root.val
  return false if r && r < root.val

  is_valid_bst(root.left, l, root.val - 1) &&
  is_valid_bst(root.right, root.val + 1, r)
end