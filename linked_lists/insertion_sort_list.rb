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

  p = dummy = ListNode.new(nil)
  cur = dummy.next = head

  while cur && cur.next
    key = cur.next.val

    # keep navigating the list as long as key > current element
    if cur.val < key
      cur = cur.next
      next
    end

    # Make prev point to the starting element and then keep
    # moving until we find the last element less than key
    p = dummy if p.next.val > key
    p = p.next while p.next.val < key

    # swap the key element after p element
    new = cur.next
    cur.next = new.next
    new.next = p.next
    p.next = new
  end

  dummy.next
end