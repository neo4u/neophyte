# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @param {Integer} n
# @return {ListNode}
def remove_nth_from_end(head, n)
    dummy = ListNode.new(nil)
    dummy.next = head
    slow = fast = dummy
    
    (n + 1).times { |i| fast = fast.next }
    fast, slow = fast.next, slow.next while fast
    slow.next = slow.next.next ? slow.next.next : nil

    dummy.next
end

# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Approach 1: Two pass
# Aprroach 2: One Pass
# We use two pointers slow and fast
# We iterate n + 1 times and advance fast
# So fast is n nodes ahead of slow
# Now we advance slow and fast until fast hits the end
# At this point slow is pointing to the nth node.
# We swap slow.next and slow.next.next
# We return the dummy.next pointing to the head

# Complexity Analysis
# Time complexity : O(L), The algorithm makes one traversal of the list of LL nodes.
#                   Therefore time complexity is O(L)O(L).
# Space complexity : O(1), We only used constant extra space.