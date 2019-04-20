# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# Encodes a tree to a single string.
# @param {TreeNode} root
# @return {string}
def serialize(root)
    pre_order = []
    dfs_serialize(root, pre_order)
    pre_order.join(",")
end

def dfs_serialize(node, pre_order)
    if !node
        pre_order.push("#")
        return
    end

    pre_order.push(node.val.to_s)
    dfs_serialize(node.left, pre_order)
    dfs_serialize(node.right, pre_order)
end


# Decodes your encoded data to tree.
# @param {string} data
# @return {TreeNode}
def deserialize(data)
    return if data.empty?
    pre_order = data.split(",")
    dfs_deserialize(pre_order)
end

def dfs_deserialize(pre_order)
    return if pre_order.empty?

    val = pre_order.shift()
    val == '#' ? return : val = val.to_i
    root = TreeNode.new(val)

    root.left = dfs_deserialize(pre_order)
    root.right = dfs_deserialize(pre_order)

    root
end

# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-bst/description/

# Approach 1: DFS using pre-order for serialization and DFS and Queue for deserialization
# Steps:
# 1. Serialize using pre-order traversal using depth first search and represent null by "#"
# 2. Deserialize by traversing the serialized tree string and using recursion. O(n).

# Approach 2: BFS using queue and iterative approach and pre_order
# Time: O(n), visit n nodes once
# Space: O(n), store the entire tree in array and string


require 'test/unit'
extend Test::Unit::Assertions

root = TreeNode.new(1)
l, r = TreeNode.new(2), TreeNode.new(3)
r1, r2 = TreeNode.new(4), TreeNode.new(5)
root.left, root.right = l, r
r.left, r.right = r1, r2

assert_equal(serialize(root), "1,2,#,#,3,4,#,#,5,#,#")

new_root = deserialize("1,2,#,#,3,4,#,#,5,#,#")
assert_equal(new_root.val, root.val)
assert_equal(new_root.left.val, l.val)
assert_equal(new_root.right.val, r.val)
assert_equal(new_root.right.left.val, r1.val)
assert_equal(new_root.right.right.val, r2.val)