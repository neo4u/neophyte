# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# Approach 1: DFS
# @param {TreeNode} root
# @return {TreeNode}
def invert_tree(root)
    return if root.nil?
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    root
end

# Approach 2: DFS Iterative
# @param {TreeNode} root
# @return {TreeNode}
def invert_tree_dfs_iter(root)
    stack = [root]
    while !stack.empty?
        node = stack.pop()
        next if !node
        node.left, node.right = node.right, node.left
        stack += [node.left, node.right]
    end

    root
end

# Approach 3: BFS
# @param {TreeNode} root
# @return {TreeNode}
def invert_tree_bfs(root)
    q = [root]
    while !q.empty?
        node = q.shift()
        next if !node
        node.left, node.right = node.right, node.left
        q += [node.left, node.right]
    end

    root
end

# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/

# Approach 1: DFS Recursive
# Approach 2: DFS Iterative
# Approach 3: BFS

# Time: O(n)
# Space: O(n), worst case h is O(n)

# Input:
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

require 'test/unit'
extend Test::Unit::Assertions


root = TreeNode.new(4)
node2a, node2b = TreeNode.new(2), TreeNode.new(7)
root.left, root.right = node2a, node2b

node3a, node3b, node3c, node3d = TreeNode.new(1), TreeNode.new(3), TreeNode.new(6), TreeNode.new(9)
node2a.left, node2a.right, node2b.left, node2b.right = node3a, node3b, node3c, node3d

new_root = invert_tree(root)
assert_equal(new_root.val, 4)
assert_equal(new_root.left.val, 7)
assert_equal(new_root.right.val, 2)

assert_equal(new_root.left.left.val, 9)
assert_equal(new_root.left.right.val, 6)

assert_equal(new_root.right.left.val, 3)
assert_equal(new_root.right.right.val, 1)


root = TreeNode.new(4)
node2a, node2b = TreeNode.new(2), TreeNode.new(7)
root.left, root.right = node2a, node2b

node3a, node3b, node3c, node3d = TreeNode.new(1), TreeNode.new(3), TreeNode.new(6), TreeNode.new(9)
node2a.left, node2a.right, node2b.left, node2b.right = node3a, node3b, node3c, node3d

new_root = invert_tree_dfs_iter(root)
assert_equal(new_root.val, 4)
assert_equal(new_root.left.val, 7)
assert_equal(new_root.right.val, 2)

assert_equal(new_root.left.left.val, 9)
assert_equal(new_root.left.right.val, 6)

assert_equal(new_root.right.left.val, 3)
assert_equal(new_root.right.right.val, 1)

root = TreeNode.new(4)
node2a, node2b = TreeNode.new(2), TreeNode.new(7)
root.left, root.right = node2a, node2b

node3a, node3b, node3c, node3d = TreeNode.new(1), TreeNode.new(3), TreeNode.new(6), TreeNode.new(9)
node2a.left, node2a.right, node2b.left, node2b.right = node3a, node3b, node3c, node3d

new_root = invert_tree_bfs(root)
assert_equal(new_root.val, 4)
assert_equal(new_root.left.val, 7)
assert_equal(new_root.right.val, 2)

assert_equal(new_root.left.left.val, 9)
assert_equal(new_root.left.right.val, 6)

assert_equal(new_root.right.left.val, 3)
assert_equal(new_root.right.right.val, 1)