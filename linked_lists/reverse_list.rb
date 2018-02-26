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
def reverse_list(head)
  cur, prv = head, nil
  cur.next, cur, prv = prv, cur.next, cur while cur

  prv
end
