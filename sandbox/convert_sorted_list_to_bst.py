# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return
        if not head.next: return TreeNode(head.val)

        mid = self.find_mid(head)
        root = TreeNode(mid.val)
        l, r = head, mid.next
        root.left, root.right = self.sortedListToBST(l), self.sortedListToBST(r)

        return root

    def find_mid(self, head):
        prev, slow, fast = None, head, head

        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None

        return slow
