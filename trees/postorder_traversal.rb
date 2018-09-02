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
def postorder_traversal(root)
  result = []
  dfs(root, result)
  result
end

def dfs(node, result)
  return if node.nil?

  dfs(node.left, result)
  dfs(node.right, result)
  result.push(node.val)
end
