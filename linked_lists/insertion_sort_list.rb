# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val)
        @val = val
        @next = nil
    end
end

def insertion_sort_list(head)
    return head if !head || !head.next

    dummy = ListNode.new(-1)
    cur = head
    prv = dummy
    nxt = nil

    while cur
        nxt = cur.next
        prv = prv.next while prv.next && prv.next.val < cur.val

        cur.next = prv.next
        prv.next = cur
        prv = dummy
        cur = nxt
    end

    dummy.next
end

