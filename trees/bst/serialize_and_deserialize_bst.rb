# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right

    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

class Integer
    N_BYTES = [42].pack('i').size
    N_BITS = N_BYTES*8
    MAX = 2**(N_BITS - 2) - 1
    MIN = -MAX - 1
end

# Encodes a tree to a single string.
# @param {TreeNode} root
# @return {string}
def serialize(root)
    pre_order = []
    dfs_serialize(root, pre_order)
    pre_order.join(",")
end

def dfs_serialize(node, result)
    return if !node
    result.push(node.val.to_s)
    dfs_serialize(node.left, result)
    dfs_serialize(node.right, result)
end

# Decodes your encoded data to tree.
# @param {string} data
# @return {TreeNode}
def deserialize(data)
    return if data.empty?
    v_min, v_max = Integer::MIN, Integer::MAX
    pre_order = data.split(",")
    dfs_deserialize(pre_order, v_min, v_max)
end

def dfs_deserialize(pre_order, v_min, v_max)
    return if pre_order.empty?
    val = pre_order.first.to_i
    return if !val.between?(v_min, v_max)

    pre_order.shift()
    node = TreeNode.new(val)
    node.left = dfs_deserialize(pre_order, v_min, val)
    node.right = dfs_deserialize(pre_order, val, v_max)

    node
end

# 449. Serialize and Deserialize BST
# https://leetcode.com/problems/serialize-and-deserialize-bst/

# Key Insight
# Difference from from problem no. 297 is:
# 1. This is a BST
# 2. We need to make the serialized string as compact as possible
# 3. All we need to do is get the order of insertion into BST
#    to construct the bst,
#    we don't need to know position of leaf nodes and such and
#    hence it's as compact as possible.

# Approach 1: DFS using pre-order traversal
# Steps:
# 1. Serialize using pre-order dfs
# 2. Deserialize using pre-order traversal of array and 
#    use node bounds to find the leaves

# Time: O(n)
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

#       6
#      / \
#     4   8
#    / \
#   2   5

root = TreeNode.new(6)
l, r = TreeNode.new(4), TreeNode.new(8)
l1, l2 = TreeNode.new(2), TreeNode.new(5)
root.left, root.right = l, r
l.left, l.right = l1, l2

assert_equal(serialize(root), "6,4,2,5,8")

new_root = deserialize("6,4,2,5,8")
assert_equal(new_root.val, root.val)
assert_equal(new_root.left.val, l.val)
assert_equal(new_root.right.val, r.val)
assert_equal(new_root.left.left.val, l1.val)
assert_equal(new_root.left.right.val, l2.val)

assert_equal(serialize(nil), "")
assert_equal(deserialize(""), nil)
