class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return

        level_start = root
        while level_start:
            curr = level_start

            while curr:
                if curr.left: curr.left.next = curr.right
                if curr.right and curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next

            level_start = level_start.left

        return root

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