# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer[]} inorder
# @param {Integer[]} postorder
# @return {TreeNode}
def build_tree(inorder, postorder)
    return if inorder.nil? || postorder.nil? || inorder.empty? || postorder.empty?
    root = TreeNode.new(postorder.pop)

    idx = inorder.find_index(root.val)
    root.right = build_tree(inorder[idx + 1...inorder.size], postorder)
    root.left = build_tree(inorder[0...idx], postorder)
    
    root
end