# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def merge_two_lists(l1, l2)
  dummy = cur = ListNode.new(0)
  while l1 || l2
    if (l1 && l2 && l1.val < l2.val) || l2.nil?
      cur.next, l1 = l1, l1.next
    elsif (l1 && l2) || l1.nil?
      cur.next, l2 = l2, l2.next
    end
    cur = cur.next
  end

  dummy.next
end
