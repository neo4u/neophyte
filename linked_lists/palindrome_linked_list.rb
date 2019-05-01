# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val)
        @val = val
        @next = nil
    end
end

# @param {ListNode} head
# @return {Boolean}
def is_palindrome(head)
    fast = slow = head
    # find the mid node
    fast, slow = fast.next.next, slow.next while fast && fast.next

    # reverse the second half
    prv, cur = nil, slow
    prv, prv.next, cur = cur, prv, cur.next while cur

    # compare the first and second half nodes
    while prv # as long as prv is not nil
        return false if prv.val != head.val
        prv = prv.next
        head = head.next
    end

    true
end


# Odd case
# a,b,c,b,a
# in while fast and fast.next
# after 1 slow = b, fast = c
# after 2 slow = c, fast = a
# at 3 fast.next = nil so exit

# now prv points to c, b, a
# while prv
# 1 prv.val = a, head.val = a pass and then prv point to b, and head points to b
# 2 prv.val = b, head.val = b pass and then prv points to c, and head points to c
# we exit before 3rd iteration because prv becomes next item of c which is nil

# Even case
# a,b,c,c,b,a
# in while fast and fast.next
# after 1 slow = b, fast = c pass
# after 2 slow = c, fast = b pass
# after 3 slow = c, fast = nil
# at 4 fast = nil so exit

# now prv points to c, b, a after reversal points to a in list a, b, c
# while prv
# 1 prv.val = a, head.val = a pass and then prv point to b, and head points to b
# 2 prv.val = b, head.val = b pass and then prv points to c, and head points to c
# 3 prv.val = c, head.val = c pass and then prv points to nil, and head points to 2nd c
# We exit before 4th iteration because prv becomes next item of c which is nil


# Time: O(n)
# Space: O(1)