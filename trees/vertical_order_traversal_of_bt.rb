# Difference:
# 314. If two nodes are in the same row and column, the order should be from left to right.
# 987. If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# 987. Vertical Order Traversal of a Binary Tree


# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# @param {TreeNode} root
# @return {Integer[][]}
def vertical_order(root)
    return [] if !root
    q, level_map = [[root, 0]], Hash.new { |h, k| h[k] = [] }
    min, max = 0, 0

    while !q.empty?
        node, level = q.shift
        level_map[level].push(node.val)

        min = level if level < min
        max = level if level > max

        q.push([node.left, level - 1]) if node.left
        q.push([node.right, level + 1]) if node.right
    end

    min.upto(max).map { |i| level_map[i] }
end