# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {ListNode}
def reverse_list(head)
  cur, prv = head, nil
  prv, prv.next, cur = cur, prv, cur.next while cur
  prv
end

# # Recursive solution, a lil slower
# def reverse_list(head)
#   _reverse(head)
# end

# def _reverse(node, prv = nil)
#   return prv unless node
#   nxt = node.next
#   node.next = prv
#   _reverse(nxt, node)
# end
