# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {Void} Do not return anything, modify head in-place instead.
def reorder_list(head)
    return if !head || !head.next
    h1, h2 = split_list(head)
    h2 = reverse_list(h2)
    merge_lists(h1, h2)
end

def split_list(head)
    [head, find_middle(head)]
end

def find_middle(head)
    slow, fast = head, head

    while fast && fast.next
        slow, fast = slow.next, fast.next.next
    end
    mid, slow.next = slow.next, nil

    mid
end

def reverse_list(head)
    prv, cur = nil, head

    while cur
        tmp = cur.next
        cur.next = prv
        prv = cur
        cur = tmp
    end

    prv
end

def merge_lists(h1, h2)
    head = tmp = h1
    h1 = h1.next # Advance the first list as first node is in final place

    while h1 && h2
        # Link h2 as next node and advance tmp and h2
        tmp.next = h2
        tmp = tmp.next
        h2 = h2.next

        # Link h1 as next node and advance tmp and h1
        tmp.next = h1
        tmp = tmp.next
        h1 = h1.next
    end

    tmp.next = h1 || h2 # Attach remaining part of non-nil list without alternating
    head
end

# Alternative merge with lesser lines but hard to understand
# Technique is to swap h1 and h2 at the end of iteration and
# keep performing the loop on h2
def merge_lists(h1, h2)
    head = tmp = h1
    h1 = h1.next # Advance the first list as first node is in final place

    while h2
        tmp.next = h2
        tmp = tmp.next
        h2 = h2.next

        h1, h2 = h2, h1 if h1
    end

    head
end