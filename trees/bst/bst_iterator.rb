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

# Intuition
# 1. Iterating nodes of a BST is nothing but getting nodes in an in-order traversal order
# 2. We need some temp storage for nodes

# Approach 1: Simple list to store all elements (Sub-Optimal)
# Steps:
# 1. Save all elements in a list at init doing an inorder traversal, (left, root, right)
# 2. Keep popping from the list to provide for next.

# Time: next(): O(1), has_next(): O(1), init: ()
# Space: O(n)

# Approach 2: Using Stack
# Steps:
# 1. We keep a stack and at init we push the entire left sub-tree in reverse order
#    Like so, save root, root.left, root.left.left ... and so on until leaf node
# 2. When next is called, we pop the stack push the right sub-tree of the popped node
#    and return the value at the node
# 3. For hasNext() we just return if there are any nodes left in the stack
# 4. For push_left, we just iteratively push nodes into the stack
#    and move to the left node until the leaf

# Time: init: O(log(n)) cuz we only iterate down the left sub-tree
#       next(): O(1) per call, called n times
#       has_next(): O(1)
# Space: O(n)
