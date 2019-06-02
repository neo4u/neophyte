# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {String[]}
def binary_tree_paths(root)
    @paths = []
    dfs(root)
    @paths
end

def dfs(node, path = [])
    return if !node  # Corner case when root itself is null, no leaf node
    path = path + [node.val]

    # As soon as we encounter a leaf node, push the path so far into paths list
    if !node.left && !node.right
        @paths << path.join('->')
    # For all other cases, just traverse down left and right children
    else
        dfs(node.left, path)
        dfs(node.right, path)
    end
end

# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/

# Time: O(n)
# Space: Avg O(log(n)), Worst case O(n), Based on the depth of the tree for call stack.