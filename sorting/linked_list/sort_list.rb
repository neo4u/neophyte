# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} head
# @return {ListNode}
def sort_list(head)
  return head if head.nil? || head.next.nil?
  mid = find_mid(head)
  l, r = head, mid

  merge(sort_list(l), sort_list(r))
end

def find_mid(head)
  pre, slow, fast = nil, head, head
  while fast && fast.next
    pre, slow, fast = slow, slow.next, fast.next.next
  end
  pre.next = nil

  slow
end

def merge(l, r)
  # return the non-nil part if one of them is nil
  return l || r if !l || !r

  # This is the actual part that does the sorting when list size is 1
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

# 148. Sort List

# Sort a linked list in O(n log n) time using constant space complexity.
# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4

# Example 2:
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

n1 = ListNode.new(4)
n2 = ListNode.new(2)
n3 = ListNode.new(1)
n4 = ListNode.new(3)
# n5 = ListNode.new(5)

n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n5

m1 = ListNode.new(1)
m2 = ListNode.new(2)
m3 = ListNode.new(3)
m4 = ListNode.new(4)

m1.next = m2
m2.next = m3
m3.next = m4

require 'test/unit'
extend Test::Unit::Assertions

sorted = sort_list(n1)
while sorted && m1
  assert_equal(sorted.val, m1.val)
  sorted = sorted.next
  m1 = m1.next
end

