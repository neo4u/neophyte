class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.push_left(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

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

# I use Stack to store directed left children from root.
# When next() be called, I just pop one element and process its right child as new root.
# The code is pretty straightforward.

# So this can satisfy O(h) memory, hasNext() in O(1) time,
# But next() is O(h) time.

# I can't find a solution that can satisfy both next() in O(1) time, space in O(h).