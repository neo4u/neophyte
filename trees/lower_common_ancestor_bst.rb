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
    return root if root.nil? || root == p || root == q

    return lowest_common_ancestor(root.left, p, q) if p.val < root.val && q.val < root.val
    return lowest_common_ancestor(root.right, p, q) if p.val > root.val && q.val > root.val

    root
end

# Approach 2: Iterative
def lowest_common_ancestor(root, p, q)
    while root
        if p.val < root.val && q.val < root.val
            root = root.left
        elsif root.val < p.val && root.val < q.val
            root = root.right
        else
            return root
        end
    end
end


# Approach 1: Recursive
# Approach 2: Iterative