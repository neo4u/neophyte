class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Follow up: Please reverse the list into K Group
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count, curr = 0, head

        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k: return head

        last_head, curr_head = self.reverse_k(head, count)
        head.next = self.reverseKGroup(curr_head, k)
        return last_head

    def reverse_k(self, head, k):
        prev, curr = None, head

        while k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1

        return prev, curr


# class Solution:
#     def reverseList(self, head):
#         if not head or not head.next:
#             return head

#         prev, cur, nxt = None, head, head
#         while cur:
#             nxt = cur.next
#             cur.next = prev
#             prev = cur
#             cur = nxt
#         return prev

# 25. Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/


def print_list(head):
    s = ""
    while head:
        s += f"{head.val}->"
        head = head.next

    print(s)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()
print_list(sol.reverseKGroup(node1, 2))

# 2->1->4->3->5->
# 1->2->3->null

# null <- 1 <- 2-> 3
