class ListNode
    attr_accessor :val, :next
    def initialize(val)
        @val = val
        @next = nil
    end
end

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

# Approach 5: Divide and Conquer (Merge Sort Way)
# @param {ListNode[]} lists
# @return {ListNode}
def merge_k_lists(lists, s_idx = 0, e_idx = lists.size - 1)
    return if lists.empty?
    return lists[e_idx] if s_idx == e_idx

    mid = (s_idx + e_idx) / 2
    left = merge_k_lists(lists, s_idx, mid)
    right = merge_k_lists(lists, mid + 1, e_idx)

    merge_two_lists(left, right)
end

def merge_two_lists(l1, l2)
    dummy = curr = ListNode.new(nil)

    while l1 || l2
        if (l1 && l2 && l1.val < l2.val) || !l2
            curr.next, l1 = l1, l1.next
        elsif (l1 && l2) || !l1
            curr.next, l2 = l2, l2.next
        end
        curr = curr.next
    end

    dummy.next
end

# Approach 6: Divide and Conquer, Iterative
# @param {ListNode[]} lists
# @return {ListNode}
def merge_k_lists(lists)
    k, interval = lists.size, 1

    while interval < k
        0.step(k - interval, interval * 2) do |i|
            l, r = lists[i], lists[i + interval]
            lists[i] = merge_two_lists(l, r)
        end
        interval *= 2
    end

    k > 0 ? lists.first : lists
end

def merge_two_lists(l1, l2)
    dummy = curr = ListNode.new(nil)

    while l1 || l2
        if (l1 && l2 && l1.val < l2.val) || !l2
            curr.next, l1 = l1, l1.next
        elsif (l1 && l2) || !l1
            curr.next, l2 = l2, l2.next
        end
        curr = curr.next
    end

    dummy.next
end

# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/

# There are 5 approaches
# Approach 1: Brute force, collect all nodes and sort by value. Approach from above.
# Time: O(nlog(n))
# Space: O(n)

# Approach 2: Iterate through all the lists and take the minimum from the k lists 
# Time: O(k * n)
# Space: O(1)

# Approach 3: The comparison process can be optimized in the above process using priority queue.
# Time: O(nlogk)
# Space: O(1)

# Approach 4: Divide and Conquer, Merge k lists k-1 times two at a time.
# Time: O(nk)
# Space: O(1)

# Approach 5: Divide and Conquer, Merge sort way (Optimal)
# Time: O(nlogk)
# Space: O(log(k)), log(k) for stack

# Approach 6: Divide and Conquer, Iterative
# Time: O(nlogk)
# Space: O(1)
