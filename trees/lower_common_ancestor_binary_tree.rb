# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# Approach 1: Recursive
# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)
    return root if !root || root == p || root == q

    l = lowest_common_ancestor(root.left, p, q)
    r = lowest_common_ancestor(root.right, p, q)

    return root if l && r
    l || r
end

# Approach 2: Iterative
def lowest_common_ancestor(root, p, q)
    stack = [root]
    parent = { root => nil }

    while !parent.key?(p) || !parent.key?(q)
        node = stack.pop()
        if node.left
            parent[node.left] = node
            stack.push(node.left)
        end

        if node.right
            parent[node.right] = node
            stack.push(node.right)
        end
    end

    ancestors = Set.new()
    while p
        ancestors.add(p)
        p = parent[p]
    end

    while !ancestors.include?(q)
        q = parent[q]
    end

    q
end

# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


# Approach 1: Recursive
# Approach 2: Iterative