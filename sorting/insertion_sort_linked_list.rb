# def insertionSortList(self, head):
#   p = dummy = ListNode(0)
#   cur = dummy.next = head
  # while cur and cur.next:
  #     val = cur.next.val
  #     if cur.val < val:
  #         cur = cur.next
  #         continue
  #     if p.next.val > val:
  #         p = dummy
  #     while p.next.val < val:
  #         p = p.next
  #     new = cur.next
  #     cur.next = new.next
  #     new.next = p.next
  #     p.next = new
  # return dummy.next

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
def insertion_sort_list(head)
  return head if head.nil? || head.next.nil?

  p = dummy = ListNode.new(nil)
  cur = dummy.next = head

  while cur && cur.next
    val = cur.next.val
    if cur.val < val
      cur = cur.next
      next
    end

    p = dummy if p.next.val > val
    p = p.next while p.next.val < val

    new = cur.next
    cur.next = new.next
    new.next = p.next
    p.next = new
  end

  dummy.next
end
