class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return None

        head, tail = self.dfs(root)
        head.left, tail.right = tail, head
        return head

    def dfs(self, root):
        if not root.left and not root.right: # Find leaf nodes
            return root, root

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
