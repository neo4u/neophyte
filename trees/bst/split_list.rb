# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} v
# @return {TreeNode[]}
def split_bst(root, v)
    return [nil, nil] if root.nil?
    
    if v < root.val
        parts = split_bst(root.left, v)
        root.left = parts[1]
        [parts[0], root]
    else
        parts = split_bst(root.right, v)
        root.right = parts[0]
        [root, parts[1]]
    end
end


# V = 2
#           4
#         /   \
#       2      6
#      / \    / \
#     1   3  5   7

# split_bst(4, 2)
#     2 < root.val so go left
#     split_bst(2, 2)
#         2 == root.val so go right
#         split_bst(3, 2)
#             2 < root.val so go left
#             split_bst(nil, 2)
#             [nil, nil]
#         3.left == nil
#         [nil, 3]
#     2.right = nil
#     [2, 3]
# 4.left = 3
# [2, 4]


# V = 5
#           4
#         /   \
#       2      6
#      / \    / \
#     1   3  5   7

# split_bst(4, 5)
#     5 >= root.val so go right
#     split_bst(6, 5)
#         5 < root.val so go left
#         split_bst(5, 5)
#             5 >= root.val so go right
#             split_bst(nil, 5)
#             [nil, nil]
#         5.right = parts[0] = nil
#         [5, nil]
#     6.left = nil
#     [5, 6]
# 4.right = 5
# [4, 6]

# 776. Split BST
# https://leetcode.com/problems/split-bst/description/