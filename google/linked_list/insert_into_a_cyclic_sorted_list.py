class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """

        new_node = Node(insertVal, None)
        if not head:
            new_node.next = new_node
            return new_node

        cur = head

        while not (cur.val < insertVal <= cur.next.val):
            # cur is max, and cur.next is min. If max < v or min >= v, we stop
            if cur.next.val <= cur.val:
                if cur.val < insertVal or cur.next.val >= insertVal:
                    break

            cur = cur.next

        new_node.next, cur.next = cur.next, new_node
        return head


# One Pass O(n) O(1)

# insert at the end; insert in the middle;
# insert before head (e.g. all the values are equal in the original list)
class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        new_node = Node(insertVal, head)
        
        if not head:  
            return new_node
         
        node = head
        while True:
            if node.next.val < node.val and (insertVal <= node.next.val or insertVal >= node.val):
                break
            elif node.val <= insertVal <= node.next.val:
                break
            elif node.next == head:
                break
            node = node.next

        new_node.next = node.next
        node.next = new_node
        return head

# 708. Insert into a Cyclic Sorted List
# https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/description/