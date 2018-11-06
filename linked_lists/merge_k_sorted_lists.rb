# Definition for singly-linked list.
# class ListNode
#         attr_accessor :val, :next
#         def initialize(val)
#                 @val = val
#                 @next = nil
#         end
# end

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

# Time: O(N log N) - Sorting (N log N) and iterating through all lists(N) obviously the max of them is N log N so that decides the complexity
# Space: O(N) - Sorting and list of nodes
