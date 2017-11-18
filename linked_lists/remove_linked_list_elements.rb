# Definition for singly-linked list.
# class ListNode
#   attr_accessor :val, :next
#   def initialize(val)
#     @val = val
#     @next = nil
#   end
# end

# @param {ListNode} head
# @param {Integer} val
# @return {ListNode}
def remove_elements(head, val)
  head = head.next while head && head.val == val
  return if head.nil? || val.nil?
  prv, cur = head, head.next

  while cur # If match is found link prev node to next node
    if cur.val == val
      prv.next, cur = cur.next, cur.next
    else    # If no match is found link prev node to next node
      prv, cur = cur, cur.next
    end
  end

  head
end
