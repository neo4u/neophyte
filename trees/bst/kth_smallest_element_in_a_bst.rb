# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# Approach 1: With global
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
    dfs(node.left)
    @k -= 1
    if @k.zero?
        @val = node.val
        return
    end
    dfs(node.right)
end


# Approach 2: With array
def kth_smallest(root, k)
    inorder(root, [])[k - 1]
end

def inorder(root, a)
    return a if root.nil?
    inorder(root.left, a)
    a << root.val
    inorder(root.right, a)
    a
end