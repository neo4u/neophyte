class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None

        head, tail = self.dfs(root)
        head.left, tail.right = tail, head
        return head

    def dfs(self, root):
        # if not root.left and not root.right: # Find leaf nodes
        #     return root, root

        # Note: if left / right subtree is None, root node will become the head / tail of the linked list
        # That's why variables below are initialized as root.
        l_head = l_tail = r_head = r_tail = root
        if root.left:
            l_head, l_tail = self.dfs(root.left)
            l_tail.right = root # Like setting node.next = root
            root.left = l_tail  # Like setting root.prev = l_tail

        if root.right:
            r_head, r_tail = self.dfs(root.right)
            r_head.left = root  # Like setting r_head.prev = root
            root.right = r_head # Like setting root.next = r_head

        return l_head, r_tail


# 426. Convert Binary Search Tree to Sorted Doubly Linked List
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

# Intuition
# 1. Sorted order in a BST in an inorder traversal
# 2. Inorder traversal means visit (left sub-trees, root, right sub-trees)

# Steps:
# 1. For each call to DFS with a reference to the root of a sub-tree,
#    we return the left most left and the right most left,
#    which will be the head of the list, and the tail of the list
# 2. Within the DFS, we have 4 variables which default to the root
#    l_head, l_tail, represent 1st and last nodes of the left sub-tree
#    r_head, r_tail, represent 1st and last nodes of the right sub-tree
# 3. If a left sub-tree exists, then we traverse the left sub-tree and get its 1st and last nodes
#    as l_head and l_tail, then we need to do l_tail.next to root, and root.prev to l_tail
# 4. If a right sub-tree exists, then we traverse the right sub-tree and get its 1st and last nodes
#    as r_head and r_tail, then we need to do r_tail.prev to root, and root.next to r_head
# 5. Then we need to return the first and last nodes of the current sub-tree which are, l_head, r_tail
