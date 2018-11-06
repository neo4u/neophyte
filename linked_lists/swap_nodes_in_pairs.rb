# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next

    def initialize(val)
        @val = val
        @next = nil
    end
end

# Iterative
# @param {ListNode} head
# @return {ListNode}
def swap_pairs(head)
    dummy = ListNode.new(-1)
    dummy.next = head
    curr = dummy
    
    while curr.next && curr.next.next
        first, second = curr.next, curr.next.next
        
        curr.next = second
        first.next = second.next
        second.next = first
        
        curr = curr.next.next
    end
    
    dummy.next
end

# Recursive
# @param {ListNode} head
# @return {ListNode}
def swap_pairs(head)
    return head if !head || !head.next

    n = head.next
    head.next = swap_pairs(n.next)
    n.next = head

    n
end
