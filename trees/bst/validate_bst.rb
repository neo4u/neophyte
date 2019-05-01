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
def is_valid_bst(root, l = -Float::INFINITY, r = Float::INFINITY)
    return true if !root
    return false if !root.val.between?(l, r)
    is_valid_bst(root.left, l, root.val - 1) && is_valid_bst(root.right, root.val + 1, r)
end

# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# 1. Set bounds based on parents bounds
# 2. Check if current nodes values respect the bounds set by upper layer
# 3. Recursively check if left and right sub-trees are valid bst with bounds:
#     left between l, root.val - 1
#     right between root.val + 1, r
#     where l and r are bounds for current node

# Time: O(n)
# Space: O(h), h is depth of recursion