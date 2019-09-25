class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.push_left(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) != 0

    # @return an integer, the next smallest number
    def next(self):
        tmp = self.stack.pop()
        self.push_left(tmp.right)
        return tmp.val

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left


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
