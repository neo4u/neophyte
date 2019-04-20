# Recursive
class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closest = float('inf')
        
        def helper(root, value):
            if not root:
                return
            if abs(root.val - target) < abs(self.closest - target):
                self.closest = root.val
                
            # Target should be located on left subtree
            if target < root.val:
                helper(root.left, target)
                
            # target should be located on right subtree
            if target > root.val:
                helper(root.right, target)
        
        helper(root, target)
        return self.closest

# Iterative
class Solution(object):
    def closestValue(self, root, target):
        closest = root.val
        while root:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            root = root.left if target < root.val else root.right
        return closest

# > Time Complexity O(N)
# > Space Complexity O(1)
