class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

            self.connect(root.left)
            self.connect(root.right)

        return root

    
#    1
#   /  \
#  2 -> 3
#      / \
#     4 -> 5