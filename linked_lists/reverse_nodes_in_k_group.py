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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Follow up: Please reverse the list into K Group
class Solution(object):
    def reverseKGroup(self, head, k):
        count, node = 0, head

        while node and count < k:
            node = node.next
            count += 1

        if count < k:
            return head

        new_head, prev_head = self.reverse(head, k)
        head.next = self.reverseKGroup(new_head, k)

        return prev_head

    def reverse(self, head, count):
        prev, cur, nxt = None, head, head

        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1

        return (cur, prev)

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

1->2->3->null

null <- 1 <- 2-> 3


