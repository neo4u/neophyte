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
    slow.next = slow.next.next

    dummy.next
end

# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Approach 1: Two pass
# Aprroach 2: One Pass
# - We use two pointers slow and fast
# - We also use a dummy pointer before head and set slow and fast to dummy which is 1 node before head
# - We iterate n + 1 times and advance fast
# - So fast is n nodes ahead of slow
# - Now we advance slow and fast until fast hits the end
# - At this point slow is pointing to the nth node from the end
# - We swap slow.next and slow.next.next
# - We return the dummy.next pointing to the head

# Complexity Analysis
# Time: O(L), The algorithm makes one traversal of the list of L nodes.
#             Therefore time complexity is O(L).
# Space : O(1), We only used constant extra space.