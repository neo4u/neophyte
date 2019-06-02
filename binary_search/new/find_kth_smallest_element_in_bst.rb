# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def kth_smallest(root, k)
    return root if !root
    @k, @val = k, root.val
    dfs(root)

    @val
end

def dfs(node)
    return if !node
    dfs(node.left) if node.left
    @k -= 1
    if @k.zero?
        @val = node.val
        return
    end
    dfs(node.right) if node.right
end


# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/