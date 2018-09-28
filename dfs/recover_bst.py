# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        self.firstNode = TreeNode(None)
        self.secondNode = TreeNode(None)
        self.prevNode = TreeNode(float('-inf'))
        self.traverse(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val

    def traverse(self, root):
        if root == None:
            return        
        self.traverse(root.left)
        if self.firstNode.val == None and self.prevNode.val >= root.val:
            self.firstNode = self.prevNode        
        if self.firstNode.val != None and self.prevNode.val >= root.val:
            self.secondNode = root            
        self.prevNode = root        
        self.traverse(root.right)