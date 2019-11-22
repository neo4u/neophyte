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



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head_l, prev_l, curr = root, None, None

        while head_l:
            curr = head_l
            prev_l, head_l = None, None

            while curr:
                if curr.left:
                    if prev_l:
                        prev_l.next = curr.left
                    else:
                        head_l = curr.left
                    prev_l = curr.left

                if curr.right:
                    if prev_l:
                        prev_l.next = curr.right
                    else:
                        head_l = curr.right
                    prev_l = curr.right

                curr = curr.next
        return root


# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/


# Intuition:
# 1. diff between #116 and #117 is that there is no gaurantee of completeness in #117,
#    in #116 the nodes are complete at a the last level
# 2. The solution from #117 will work for both of them, cuz it check for existence of left sub-tree and right-sub-tree


#    1
#   /  \
#  2 -> 3
#      / \
#     4 -> 5
