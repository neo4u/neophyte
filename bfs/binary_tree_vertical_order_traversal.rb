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
def vertical_order(root)
    return [] if !root
    q, node, output = [[root, 0]], root, {}

    while !q.empty?
        node, level = q.shift
        output[level] ||= []
        output[level].push(node.val)

        q.push([node.left, level - 1]) if node.left
        q.push([node.right, level + 1]) if node.right
    end

    levels = output.keys.sort()
    vert_order = []
    levels.each do |l| vert_order.push(output[l]) end

    vert_order
end

# 314. Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Approach
# Look at the diagram with same file name for better intuition
# 1. Visit each node in a BFS fashion
# 2. Append left sub-tree to 1 level before (level - 1)
# 3. Append right sub-tree to 1 level after (level + 1)
# 4. Collect nodes at each level and return them in an array

# where h is height of the tree, n is number of nodes in tree
# Time: O(nlog(h))
# Space: O(h)