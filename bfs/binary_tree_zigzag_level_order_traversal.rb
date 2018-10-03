# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[][]}
def zigzag_level_order(root)
    return [] if !root
    q, result = [[root, 0]], []
    
    while !q.empty?
        level_vals, n = [], q.size
        n.times do |i|
            node, level = q.shift
            if level.even?
                level_vals.push(node.val)
            else
                level_vals.unshift(node.val)
            end

            q.push([node.left, level + 1]) if node.left
            q.push([node.right, level + 1]) if node.right
        end
        result.push(level_vals)
    end

    result
end

# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

#         -> 1->
#     <- 2   <    3 <-
#  -> 4  > 5 >  6  >  7 ->
# <- 8 9 10 11 12 13 14 15 <-
#
# level % 2 = 0 - push to back of list
# level % 2 = 1 - push to front of list
