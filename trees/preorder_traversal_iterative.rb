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
def preorder_traversal(root)
  result, stack = [], [root]

  until stack.empty?
    node = stack.pop()
    next if node.nil?
    result << node.val

    stack.push(node.right)
    stack.push(node.left)
  end

  result
end