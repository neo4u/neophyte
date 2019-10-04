# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root: return

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            # entering this block means the current root is either p's parent or a node in p's right branch.
            left = self.inorderSuccessor(root.left, p)
            return left if left else root


# When the code runs into the else block,
# that means the current root is either p's parent or a node in p's right branch.

# If it's p's parent node, there are two scenarios:
# 1. p doesn't have right child, in this case, the recursion will eventually return null, so p's parent is the successor;
# 2. p has right child, then the recursion will return the smallest node in the right sub tree, and that will be the answer.

# If it's p's right child, there are two scenarios:
# 1. the right child has left sub tree, eventually the smallest node
#    from the left sub tree will be the answer;
# 2. the right child has no left sub tree, the recursion will return null, then the right child (root) is our answer.


# Intuitive
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # the successor is somewhere lower in the right subtree
        # successor: one step right and then left till you can
        if p.right:
            p = p.right
            while p.left: p = p.left
            return p

        # the successor is somewhere upper in the tree
        stack, inorder = [], float('-inf')

        # inorder traversal : left -> node -> right
        while stack or root:
            # 1. go left till you can
            while root:
                stack.append(root)
                root = root.left

            # 2. all logic around the node
            root = stack.pop()
            # if the previous node was equal to p, then the current node is its successor
            if inorder == p.val: return root
            inorder = root.val

            # 3. go one step right
            root = root.right

        # there is no successor
        return None

# Without comments its about 20 lines
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            p = p.right
            while p.left: p = p.left
            return p

        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if inorder == p.val: return root
            inorder = root.val
            root = root.right

        return None



# 285. Inorder Successor in BST
# https://leetcode.com/problems/inorder-successor-in-bst/description/
