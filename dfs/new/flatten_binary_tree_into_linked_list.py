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

# This solution is adapted from this Java solution.
# You basically maintain a global variable prev which stores the last node that was flattened.
# First you flatten root.right, after which prev is root.right.
# Then you flatten root.left, which gets called recursively until you hit the 'end',
# at which point the flattened root.right is attached to the right of the 'end',
# and finally prev gets set to root.left. After the recursive calls,
# root.right get set to root.left, which already has the root.right attached to its end.
