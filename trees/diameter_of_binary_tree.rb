# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer}
def diameter_of_binary_tree(root)
    @result = 1

    dfs(root)
    @result - 1 # result has number of nodes in longest path, -1 of the gives us edges
end

def dfs(node)
    return 0 if !node

    l, r = dfs(node.left), dfs(node.right)
    @result = [@result, l + r + 1].max

    [l, r].max + 1 # return length of the longer sub-tree + 1
end


# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# We subtract 1 from the result because diameter of a tree doesn't count the number of nodes in the diameter.
# If you look at the description,
# "The diameter of a binary tree is the length of the longest path between any two nodes in a tree"
# Note: The length of path between two nodes is represented by the number of edges between them.
# Example:
# Given a binary tree
#     1
#    /  \
#   2    3
#  /  \
# 4    5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# It's returning 3. But the number of nodes in the diameter is 4. but the edges between them are 3. Hence the return value is 3

# Time: O(n), visits n nodes
# Space: O(log(n)), call stack worst case can be O(n) based on the skew of nodes in the tree
