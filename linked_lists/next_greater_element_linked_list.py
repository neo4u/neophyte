from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        pos, stack, result = -1, [], []

        while head:
            pos += 1
            result.append(0)

            while stack and stack[-1][1] < head.val:
                result[stack.pop()] = head.val

            stack.append((pos, head.val))
            head = head.next

        return result


# 1019. Next Greater Node In Linked List
# https://leetcode.com/problems/next-greater-node-in-linked-list/description/


# Steps:
# 1. Traverse the linked list till you reach the end of it
# 2. While head is non-null, increment the pos and append a zero to the result
# 3. Similar to next greater element I, we keep popping from the stack,
#    as long as it is less than the current node.val
# 4. We keep moving ahead in the list till it reaches the end
