# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    carry = 0
    head = ListNode.new(-1)
    s1, s2 = [], []

    while l1
        s1.push(l1.val)
        l1 = l1.next
    end

    while l2
        s2.push(l2.val)
        l2 = l2.next
    end

    while !s1.empty? || !s2.empty?
        v1, v2 = 0, 0

        v1 = s1.pop() if !s1.empty?
        v2 = s2.pop() if !s2.empty?

        carry, val = (v1 + v2 + carry).divmod(10)
        head.val = val
        temp = head

        head = ListNode.new(-1)
        head.next = temp
    end

    head.val = carry if !carry.zero?
    head.val != -1 ? head : head.next
end

# 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/description/