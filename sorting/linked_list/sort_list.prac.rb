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

  middle = find_middle(head)
  first_half, second_half, middle.next = head, middle.next, nil
  l, r = sort_list(first_half), sort_list(second_half)

  merge(l, r)
end

def find_middle(head)
  slow, fast = head, head

  while fast && fast.next && fast.next.next
    fast = fast.next.next
    slow = slow.next
  end

  slow
end

def merge(l, r)
  return l || r if l.nil? || r.nil?

  l, r = r, l if l.val > r.val

  tmp = head = l
  l = l.next

  while l && r
    if l.val < r.val
      tmp.next, l = l, l.next
    else
      tmp.next, r = r, r.next
    end
    tmp = tmp.next
  end
  tmp.next = l || r

  head
end

# 148. Sort List

# Sort a linked list in O(n log n) time using constant space complexity.
# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4

# Example 2:
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5