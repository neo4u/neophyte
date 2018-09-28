# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# @param {TreeNode} root
# @return {Void} Do not return anything, modify root in-place instead.
def recover_tree(root)
    @first = TreeNode.new(nil)
    @second = TreeNode.new(nil)
    @prev = TreeNode.new(-Float::INFINITY)

    dfs(root)
    @first.val, @second.val = @second.val, @first.val
end

# In-Order traversal
def dfs(node)
    return nil if !node

    dfs(node.left) # Process left

    # Process node
    @first = @prev if !@first.val && @prev.val >= root.val
    @second = node if @first.val && @prev.val >= root.val
    @prev = node

    dfs(node.right) # Process right
end

# Time: O(n)
# O(V + E) due to dfs
# => O(n + n - 1) due to tree
# => O(n)

# Space: O(n) due to Stack
# For O(1) you need Morris Threading Traversal which is hard.
