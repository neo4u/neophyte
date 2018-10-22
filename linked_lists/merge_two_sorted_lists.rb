# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# Itervative
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def merge_two_lists(l1, l2)
    dummy = cur = ListNode.new(0)
    while l1 || l2
        if (l1 && l2 && l1.val < l2.val) || l2.nil?
            cur.next, l1 = l1, l1.next
        elsif (l1 && l2) || l1.nil?
            cur.next, l2 = l2, l2.next
        end
        cur = cur.next
    end

    dummy.next
end

# Recursion
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def merge_two_lists(l, r)
    return r if !l
    return l if !r

    if l.val < r.val
        l.next = merge_two_lists(l.next, r)
        l
    else
        r.next = merge_two_lists(l, r.next)
        r
    end
end

# Complexity Analysis
# Approach 1: Recursion
# Time complexity: O(n + m), Because each recursive call increments the pointer to
#                  l1 or l2 by one (approaching the dangling null at the end of each list),
#                  there will be exactly one call to mergeTwoLists per element in each list.
#                  Therefore, the time complexity is linear in the combined size of the lists.
# Space complexity: O(n + m), The first call to mergeTwoLists does not return until
#                   the ends of both l1 and l2 have been reached,
#                   so n + m stack frames consume O(n + m) space.

# Approach 2: Iteravtive
# Time complexity: O(n + m), Because exactly one of l1 and l2 is incremented on each loop iteration,
#                   the while loop runs for a number of iterations equal to the sum of the lengths
#                   of the two lists. All other work is constant, so the overall complexity is linear.
# Space complexity: O(1), The iterative approach only allocates a few pointers,
#                   so it has a constant overall memory footprint.