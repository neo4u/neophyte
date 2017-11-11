# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {Boolean}
def is_palindrome(head)
  fast = slow = head
  # find the mid node
  fast, slow = fast.next.next, slow.next while fast && fast.next

  # reverse the second half
  rev = nil
  rev, rev.next, slow = slow, rev, slow.next while slow
  # tmp = slow.next
  # slow.next = rev
  # rev = slow
  # slow = tmp

  # compare the first and second half nodes
  while rev # while node and head
    return false if rev.val != head.val
    rev = rev.next
    head = head.next
  end

  true
end
