# Brute-Force
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

# Approach 3
from Queue import PriorityQueue

class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()

        for l in lists:
            if l:
                q.put((l.val, l))

        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))

        return head.next


class Solution3(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1


# There are really 5 approaches
# 1. Brute force, collect all nodes and sort by value. Approach from above. Time: O(nlog(n)) Space: O(n)
# 2. Iterate through all the lists and take the minimum from the k lists Time: O(k * n) Space: O(1)
# 3. The comparison process can be optimized in the above process using priority queue. Solution2 above. Time: O(nlogk) Space: O(1)
# 4. Merge k lists k-1 times two at a time. Time: O(nk) Space: O(1)
# 5. Merge sort way. Using divide and conquer. This is the best solution that takes Time: O(nlogk) Space: O(1)


# Best
# Time: O(nlogk)
# Space: O(1)