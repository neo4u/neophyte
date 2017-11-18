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
def sort_list(head)
  return head if head.nil? || head.next.nil?
  fast, slow = head.next, head

  while fast && fast.next
    fast = fast.next.next
    slow = slow.next
  end

  second, slow.next = slow.next, nil
  l = sort_list(head)
  r = sort_list(second)
  merge(l, r)
end

def merge(l, r)
  return l || r if !l || !r
  l, r = r, l if l.val > r.val

  head = tmp = l
  l = l.next
  while l && r
    if l.val < r.val
      tmp.next, l = l, l.next
    else
      tmp.next, r = r, r.next
    end
    tmp = tmp.next
  end
  # if one is nil just attach the other at the end
  tmp.next = l || r
  head
end

# # Time Limit Exceeded
# # @param {ListNode} head
# # @return {ListNode}
# def sort_list(head)
#   nodes = []
#   while head
#     nodes << head
#     head = head.next
#   end
#   nodes = nodes.sort_by(&:val)
#   dummy = tmp = ListNode.new(nil)
#   nodes.each do |node|
#     tmp.next = node
#     tmp = tmp.next
#   end

#   dummy.next
# end
