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
def add_two_numbers(l1, l2)
  carry = 0
  dummy = node = ListNode.new(0)

  while l1 || l2 || !count.zero?
    v1 = v2 = 0

    v1, l1 = l1.val, l1.next if l1
    v2, l2 = l2.val, l2.next if l2

    carry, val = (v1 + v2 + carry).divmod(10)
    node.next = ListNode.new(val)
    node = node.next
  end

  dummy.next
end
