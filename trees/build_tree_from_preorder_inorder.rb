# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

def build_tree(preorder, inorder, depth = 0)
    return if preorder.nil? || inorder.nil? || preorder.empty? || inorder.empty?
    puts "#{"\t" * depth} preorder: #{preorder} inorder: #{inorder}"
    root = TreeNode.new(preorder.shift)
    idx = inorder.find_index(root.val)
    root.left = build_tree(preorder, inorder[0...idx], depth + 1)
    root.right = build_tree(preorder, inorder[idx + 1...inorder.size], depth + 1)

    root
end


require 'test/unit'
extend Test::Unit::Assertions


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

build_tree(preorder, inorder)