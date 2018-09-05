# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {ListNode}
def insertion_sort_list(head)
  return head if head.nil? || head.next.nil?

  prv = dummy = ListNode.new(nil)
  cur = dummy.next = head

  while cur && cur.next
    key = cur.next.val
    if cur.val < key
      cur = cur.next
      next
    end

    prv = dummy if prv.next.val > key		# Reset prv to the start of list if prev is point to a val > key
    prv = prv.next while prv.next.val < key	# Keep moving till we find a position after which key can be place

    tmp = cur.next
    cur.next = tmp.next
    tmp.next = prv.next
    prv.next = tmp
  end

  dummy.next
end
