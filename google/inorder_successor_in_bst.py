def inorderSuccessor(self, root, p):
    succ = None
    while root:
        if p.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ


# Only in a balanced BST O(h) = O(log n).
# In the worst case h can be as large as n.

# Recursion:
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if p.val < root.val:
            return self.inorderSuccessor(root.left,p) or root
        else:
            return self.inorderSuccessor(root.right,p)

# Iterative Inorder traversal:
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        stack = []
        trav = root
        prev = None
        while stack or trav:
            if trav:
                stack.append(trav)
                trav = trav.left
            else:
                u = stack.pop()
                if u == p:
                    prev = u
                elif prev:
                    return u
                trav = u.right
        return 