class Solution:
    def reverseBetween(self, head, m, n):
        # Empty list
        if not head: return None

        # Move the 2 ptrs to m-1th (prev) node and mth node (curr).
        # 1 -> 2 -> 3 -> 4 -> 5, m = 2, n = 4
        # m = 1, n = 3, prev = 1, curr = 2

        curr, prev = head, None
        while m > 1:
            prev = curr
            curr = curr.next
            m -= 1; n -= 1

        # The two pointers that will fix the final connections.
        tail, con = curr, prev

        # Iteratively reverse the nodes until n becomes 0.
        # 1 -> 2 -> 3 -> 4 -> 5, m = 2, n = 4
        # m = 1, n = 3, prev = 1, curr = 2
        # 1 <- 2 <- 3 <- 4    5->nil
        while n:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            n -= 1

        # Adjust the final connections as explained in the algorithm
        # 1 -> 4 -> 3 -> 2 -> 1, curr = 5, tail = 2
        if con:
            con.next = prev
        else:
            # when m = 1, con will still be nil in this case
            head = prev

        # 1 -> 4 -> 3 -> 2 -> 1, curr = 5, tail = 2
        # 1 -> 4 -> 3 -> 2 -> 5
        tail.next = curr
        return head


# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/description/


# Example:
# list: 1->2->3->4->5->nil, m = 2, n = 4

# prv is nil
# cur
# 1   ->  2   ->   3   ->    4   ->   5   ->  nil
# m = 2, n = 4, p = nil, we enter while

# Move c and make p as what c used to be
# prv     cur
# 1   ->  2   ->   3   ->    4   ->   5   ->  nil
# m = 1, n = 3, we exit while as m == 1 and not >

# We set con and tail
# prv     cur
# con     tail
# 1   ->  2   ->   3   ->    4   ->   5   ->  nil

# We reverse in place, till n == 0
#        prv  cur
# 1  <-  2     3   ->    4   ->   5   ->  nil
# n = 3  -= 1 = 2

# We reverse in place, till n == 0, n = 2
#             prv    cur
# 1  <-  2 <- 3      4   ->   5   ->  nil
# n = 2 -= 1 = 1

# We reverse in place, till n == 0, n = 1
# con                  prv    cur
# 1     <-  2 <- 3 <-  4      5   ->  nil
# # n = 1 -= 1 = 0

# conn != nil, so
# con.next = prv

# We attach to con
#                    tail   cur
# 1  -> 4 -> 3  ->    2     5   ->  nil

# We attach tail to rest
# tail.next = cur
#                     tail
# 1  -> 4 -> 3  ->    2  ->   5   ->  nil