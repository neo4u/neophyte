# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# @param {TreeNode} root
# @return {Boolean}
def is_complete_tree(root)
    nodes, i = [[root, 0]], 0

    while i < nodes.size
        node, v = nodes[i]
        i += 1
        next if !node
        nodes.push([node.left, 2*v + 1])
        nodes.push([node.right, 2*v + 2])
    end

    nodes.last[1] == nodes.size - 1
end


# 958. Check Completeness of a Binary Tree
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/