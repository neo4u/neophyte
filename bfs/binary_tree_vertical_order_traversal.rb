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
    q, map = [[root, 0]], Hash.new { |h, k| h[k] = [] }
    min, max = 0, 0

    while !q.empty?
        node, level = q.shift
        map[level].push(node.val)
        min = level if level < min
        max = level if level > max
        q.push([node.left, level - 1]) if node.left
        q.push([node.right, level + 1]) if node.right
    end
    
    (min..max).map { |i| map[i] }.reject(&:empty?)
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

require 'test/unit'
extend Test::Unit::Assertions

n1 = TreeNode.new(3)
n2l = TreeNode.new(9)
n2r = TreeNode.new(20)

n3l1 = TreeNode.new(nil)
n3l2 = TreeNode.new(nil)
n3r1 = TreeNode.new(15)
n3r2 = TreeNode.new(7)

n1.left, n1.right = n2l, n2r
n2l.left, n2l.right = n3l1, n3l2
n2r.left, n2r.right = n3r1, n3r2
output = [[nil], [9], [3, nil, 15], [20], [7]]
assert_equal(vertical_order(n1), output)
