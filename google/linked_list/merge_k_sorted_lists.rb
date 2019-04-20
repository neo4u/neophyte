require_relative './str_list'

# Definition for singly-linked list.
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

# Approach 5 (Merge Sort way)
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode[]} lists
# @return {ListNode}
def merge_k_lists(lists, s_idx = 0, e_idx = lists.size - 1)
    return if lists.empty?
    return lists[e_idx] if s_idx === e_idx

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

# Approach 5: Iterative
# @param {ListNode[]} lists
# @return {ListNode}
def merge_k_lists_iterative(lists)
    return if lists.empty?
    k, interval = lists.size, 1

    while interval < k
        0.step(k - interval, interval * 2) do |i|
            l1, l2 = lists[i], lists[i + interval]
            lists[i] = merge_two_lists(l1, l2)
        end
        interval *= 2
    end

    lists.first
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
# 1. Brute force, collect all nodes and sort by value. Approach from above. Time: O(nlog(n)) Space: O(n)
# 2. Iterate through all the lists and take the minimum from the k lists Time: O(k * n) Space: O(1)
# 3. The comparison process can be optimized in the above process using priority queue. Solution2 above. Time: O(nlogk) Space: O(1)
# 4. Merge k lists k-1 times two at a time. Time: O(nk) Space: O(1)
# 5. Recursive Merge sort way. Using divide and conquer. This is the best solution that takes Time: O(nlogk) Space: O(k), stack depth k
# 5. Iterative Merge sort way. Using divide and conquer. This is the best solution that takes Time: O(nlogk) Space: O(1), we use input lists to store

# Best
# Time: O(nlogk)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

# Recursive Tests
a1 = ListNode.new(1)
a2 = ListNode.new(2)
a3 = ListNode.new(3)
a4 = ListNode.new(4)
a1.next = a2
a2.next = a3
a3.next = a4
l1 = a1

c1 = ListNode.new(10)
c2 = ListNode.new(11)
c3 = ListNode.new(12)
c4 = ListNode.new(13)
c5 = ListNode.new(14)
c1.next = c2
c2.next = c3
c3.next = c4
c4.next = c5
l2 = c1

b1 = ListNode.new(5)
b2 = ListNode.new(6)
b3 = ListNode.new(7)
b4 = ListNode.new(8)
b5 = ListNode.new(9)
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5
l3 = b1

d1 = ListNode.new(50)
d2 = ListNode.new(60)
d3 = ListNode.new(70)
d4 = ListNode.new(80)
d1.next = d2
d2.next = d3
d3.next = d4
l4 = d1

e1 = ListNode.new(100)
l5 = e1

lists = [l1, l2, l3, l4]
assert_equal(merge_k_lists(lists), l1)
assert_equal(str_list(l1), "1->2->3->4->5->6->7->8->9->10->11->12->13->14->50->60->70->80")


a1 = ListNode.new(1)
a2 = ListNode.new(2)
a3 = ListNode.new(3)
a4 = ListNode.new(4)
a1.next = a2
a2.next = a3
a3.next = a4
l1 = a1

d1 = ListNode.new(50)
d2 = ListNode.new(60)
d3 = ListNode.new(70)
d4 = ListNode.new(80)
d1.next = d2
d2.next = d3
d3.next = d4
l4 = d1
lists = [l1, l4]
assert_equal(merge_k_lists(lists), l1)
assert_equal(str_list(l1), "1->2->3->4->50->60->70->80")

lists = []
assert_equal(merge_k_lists(lists), nil)

lists = [nil, nil]
assert_equal(merge_k_lists(lists), nil)

d1 = ListNode.new(50)
d2 = ListNode.new(60)
d3 = ListNode.new(70)
d4 = ListNode.new(80)
d1.next = d2
d2.next = d3
d3.next = d4
l4 = d1

e1 = ListNode.new(100)
l5 = e1
lists = [l4, l5]
assert_equal(merge_k_lists(lists), l4)
assert_equal(str_list(l4), "50->60->70->80->100")

# Iterative Tests
a1 = ListNode.new(1)
a2 = ListNode.new(2)
a3 = ListNode.new(3)
a4 = ListNode.new(4)
a1.next = a2
a2.next = a3
a3.next = a4
l1 = a1

c1 = ListNode.new(10)
c2 = ListNode.new(11)
c3 = ListNode.new(12)
c4 = ListNode.new(13)
c5 = ListNode.new(14)
c1.next = c2
c2.next = c3
c3.next = c4
c4.next = c5
l2 = c1

b1 = ListNode.new(5)
b2 = ListNode.new(6)
b3 = ListNode.new(7)
b4 = ListNode.new(8)
b5 = ListNode.new(9)
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5
l3 = b1

d1 = ListNode.new(50)
d2 = ListNode.new(60)
d3 = ListNode.new(70)
d4 = ListNode.new(80)
d1.next = d2
d2.next = d3
d3.next = d4
l4 = d1

e1 = ListNode.new(100)
l5 = e1

lists = [l1, l2, l3, l4]
assert_equal(merge_k_lists_iterative(lists), l1)
assert_equal(str_list(l1), "1->2->3->4->5->6->7->8->9->10->11->12->13->14->50->60->70->80")

a1 = ListNode.new(1)
a2 = ListNode.new(2)
a3 = ListNode.new(3)
a4 = ListNode.new(4)
a1.next = a2
a2.next = a3
a3.next = a4
l1 = a1

d1 = ListNode.new(50)
d2 = ListNode.new(60)
d3 = ListNode.new(70)
d4 = ListNode.new(80)
d1.next = d2
d2.next = d3
d3.next = d4
l4 = d1
lists = [l1, l4]
assert_equal(merge_k_lists_iterative(lists), l1)
assert_equal(str_list(l1), "1->2->3->4->50->60->70->80")

lists = []
assert_equal(merge_k_lists_iterative(lists), nil)

lists = [nil, nil]
assert_equal(merge_k_lists_iterative(lists), nil)

d1 = ListNode.new(50)
d2 = ListNode.new(60)
d3 = ListNode.new(70)
d4 = ListNode.new(80)
d1.next = d2
d2.next = d3
d3.next = d4
l4 = d1

e1 = ListNode.new(100)
l5 = e1
lists = [l4, l5]
assert_equal(merge_k_lists_iterative(lists), l4)
assert_equal(str_list(l4), "50->60->70->80->100")
