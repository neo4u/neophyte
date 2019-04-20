class Solution(object):
    prev = None

    def flatten(self, root):
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root

# without global, In-order traversal
class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        '''
        1. flatten left subtree
        2. find left subtree's tail
        3. flatten the original right subtree
        4. set root's left to None, root's right to root'left, tail's right to root.right
        '''
        # escape condition
        if not root: return
        tmp = root.right
        # flatten right subtree
        self.flatten(tmp)

        if not root.left: return
        if not root.right and not root.left: return

        # flatten left subtree
        self.flatten(root.left)
        # find the tail of left subtree
        tail = root.left
        while tail.right:
            tail = tail.right
        # left <-- None, right <-- left, tail's right <- right
        root.left, root.right, tail.right = None, root.left, tmp


# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


# This solution is adapted from this Java solution.
# You basically maintain a global variable prev which stores the last node that was flattened.
# First you flatten root.right, after which prev is root.right.
# Then you flatten root.left, which gets called recursively until you hit the 'end',
# at which point the flattened root.right is attached to the right of the 'end',
# and finally prev gets set to root.left. After the recursive calls,
# root.right get set to root.left, which already has the root.right attached to its end.
