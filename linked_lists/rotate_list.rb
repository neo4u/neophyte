# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next

    def initialize(val)
        @val = val
        @next = nil
    end
end

# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def rotate_right(head, k)
    n = get_len(head)
    return head if !head || k.zero?
    k %= n
    slow, fast = head, head

    until k.zero?
        fast = fast.next
        k -= 1
    end

    while fast.next
        slow, fast = slow.next, fast.next
    end

    fast.next = head
    head = slow.next
    slow.next = nil

    head
end

def get_len(head)
    n = 0
    n, head = n + 1, head.next while head

    n
end


# 61. Rotate List
# https://leetcode.com/problems/rotate-list/description/

# Approach 1: Slow and Fast pointers
# Steps:
# 1. Have a slow and fast pointer
# 2. Advance the fast pointer by k nodes
# 3. Advance slow and fast pointers until fast.next == nil
#    when fast.next hits the end, slow is pointing to kth node from the end
# 4. Make fast.next point to head.
# 5. Make slow.next as new head.
# 6. Make slow.next as None.

# Example
#   k = 2
#   1->2->3->4->5->nil
#   ^
#   head
#   slow
#   fast

#   after 2.times fast = fast.next
#   1->2->3->4->5->nil
#   ^     ^
#   head  fast
#   slow
  
#   now we do slow, fast = slow.next, fast.next until fast.next == nil, at which point:
#   1->2->3->4->5->nil
#   ^     ^     ^
#   head  slow  fast

# Pointer manipulation
# fast.next = head
# head = slow.next
# slow.next = nil

require 'test/unit'
extend Test::Unit::Assertions

node1, node2, node3 = ListNode.new(1), ListNode.new(2), ListNode.new(3)
node4, node5 = ListNode.new(4), ListNode.new(5)

node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
node5.next = nil

head = rotate_right(node1, 2)

assert_equal(head.val, 4)
assert_equal(head.next.val, 5)
assert_equal(head.next.next.val, 1)
assert_equal(head.next.next.next.val, 2)
assert_equal(head.next.next.next.next.val, 3)
assert_equal(head.next.next.next.next.next, nil)


node1, node2, node3 = ListNode.new(0), ListNode.new(1), ListNode.new(2)
node1.next, node2.next, node3.next = node2, node3, nil

head = rotate_right(node1, 4)

assert_equal(head.val, 2)
assert_equal(head.next.val, 0)
assert_equal(head.next.next.val, 1)
assert_equal(head.next.next.next, nil)
