# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# Approach 1: Using shift and inorder traversal for one-time iteration.
class BSTIterator
    # @param {TreeNode} root
    def initialize(root)
        @list = inorder(root)
    end

    # @return {Boolean}
    def has_next
        !@list.empty?
    end

    # @return {Integer}
    def next
        @list.shift
    end

    private
    def inorder(root, visited = [])
        return [] if !root
        inorder(root.left, visited)
        visited << root.val
        inorder(root.right, visited)
    
        visited
    end
end

# Approach 2: Using array index for multiple iterations
class BSTIterator
    # @param {TreeNode} root
    def initialize(root)
        @list = inorder(root)
    end

    # @return {Boolean}
    def has_next
        !@list.empty?
    end

    # @return {Integer}
    def next
        @list.shift
    end

    private
    def inorder(root, visited = [])
        return [] if !root

        inorder(root.left, visited)
        visited << root.val
        inorder(root.right, visited)
    
        visited
    end
end

# Your BSTIterator will be called like this:
# i, v = BSTIterator.new(root), []
# while i.has_next()
#    v << i.next
# end

173. Binary Search Tree Iterator