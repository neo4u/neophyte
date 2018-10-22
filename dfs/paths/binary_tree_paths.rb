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

def dfs(node, visited = [])
    return if node.nil?  # Corner case when root itself is null, no leaf node
    node_val = node.val

    # As soon as we encounter a leaf node, push the path so far into paths list
    if !node.left && !node.right
        visited << node_val
        @paths << visited.join('->')
    # For all other cases, just traverse down left and right children
    else
        node_val
        dfs(node.left, visited + [node_val])
        dfs(node.right, visited + [node_val])
    end
end

# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/

# Time: O(n)
# Space: Avg O(log(n)), Worst case O(n), Based on the depth of the tree for call stack.