# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[]}
def inorder_traversal(root)
  result = []
  dfs(root, result)
  result
end

def dfs(node, result)
  return if node.nil?

  dfs(node.left, result)
  result.push(node.val)
  dfs(node.right, result)
end
