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
    result = dfs(root, 0, [])

    
    1.step(n - 1, 2) do |i|
        result[i].reverse()
    end

    result
end

def dfs(root, level, res)
    return res if !root # Ends up returning everything at the bottom of the tree
    res[level] ||= []
    res[level] << root.val
    dfs(root.left, level + 1, res)
    dfs(root.right, level + 1, res)
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
