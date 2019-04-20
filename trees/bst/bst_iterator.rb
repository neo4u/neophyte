# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

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

class BSTIterator
    def initialize(root)
        @stack = []
        push_root_to_left(root)
    end

    def next()
        root = @stack.pop
        push_root_to_left(root.right)
        root.val
    end

    def has_next()
        !@stack.empty?
    end
    
    private
    def push_root_to_left(root)
        while root
            @stack.push(root)
            root = root.left
        end
    end
end

# Your BSTIterator will be called like this:
# i, v = BSTIterator.new(root), []
# while i.has_next()
#    v << i.next
# end

# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/

# Approach 1: Simple list to store all elements (Sub-Optimal)
# Steps:
# 1. Save all elements in a list at init doing an inorder traversal, (left, root, right)
# 2. Keep popping from the list to provide for next.

# Time: next(): O(1), has_next(): O(1), init: ()
# Space: O(n)

# Approach 2: Using Stack to get nodes on demand
# Steps:
# 1. Save root, root.left, root.left.left ... and so on until leaf node
#    into stack in order to get left leaf as the first pop from the stack.
# 2. Each time next() is called pop the node on top of stack,
#    check if it has a right sub-tree and recursively push the
#    right sub-tree using the first step

# Time: next(): O(1) per call, called n times | has_next(): O(1) | init: O(log(n)) cuz we only iterate down the left sub-tree
# Space: O(log(n)), The max depth of tree will be max size of the stack

# Example