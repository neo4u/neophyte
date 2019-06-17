# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        nodes = set(G)
        prev, curr, count = head, head, 0

        while curr:
            while curr and curr.val in nodes:
                prev = curr
                curr = curr.next

            if prev.val in nodes:
                count += 1

            if not curr: break

            prev = curr
            curr = curr.next

        return count


class Solution2:
    def numComponents(self, head, G):
        G = set(G)
        count = 0
        connected = False
        while head:
            if head.val in G:
                if not connected:
                    connected = True
                    count += 1
            else:
                connected = False
            head = head.next
        return count

# [3,4,0,2,1]
# [4]

# 817. Linked List Components
# https://leetcode.com/problems/linked-list-components/description/