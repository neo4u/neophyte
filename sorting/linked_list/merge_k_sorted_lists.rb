# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# Approach 1 (Brute-Force)
# @param {ListNode[]} lists
# @return {ListNode}
def merge_k_lists(lists)
    nodes = []
    lists.each do |l|
        while l
            nodes << l
            l = l.next
        end
    end
  
    nodes = nodes.sort_by(&:val)
    dummy = tmp = ListNode.new(nil)
    nodes.each do |node|
        tmp.next = node
        tmp = tmp.next
    end
  
    dummy.next
end

# Approach 5 (Merge Sort way)
# @param {ListNode[]} lists
# @return {ListNode}
def merge_k_lists(lists, beginIndex = 0, endIndex = lists.length - 1)
    return nil if lists.length == 0
    return lists[endIndex] if beginIndex === endIndex
  
    mid = ((beginIndex + endIndex)/ 2).floor
    left = merge_k_lists(lists, beginIndex, mid)
    right = merge_k_lists(lists, mid + 1, endIndex)
  
    return merge_two_lists(left, right)
end

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

# There are really 5 approaches
# 1. Brute force, collect all nodes and sort by value. Approach from above. Time: O(nlog(n)) Space: O(n)
# 2. Iterate through all the lists and take the minimum from the k lists Time: O(k * n) Space: O(1)
# 3. The comparison process can be optimized in the above process using priority queue. Solution2 above. Time: O(nlogk) Space: O(1)
# 4. Merge k lists k-1 times two at a time. Time: O(nk) Space: O(1)
# 5. Merge sort way. Using divide and conquer. This is the best solution that takes Time: O(nlogk) Space: O(1)

# Best
# Time: O(nlogk)
# Space: O(1)