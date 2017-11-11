# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)
  return lowest_common_ancestor(root.left, p, q) if p.val < root.val && q.val < root.val
  return lowest_common_ancestor(root.right, p, q) if p.val > root.val && q.val > root.val
  root
end
