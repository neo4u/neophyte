# Definition for singly-linked list.
# class ListNode
#   attr_accessor :val, :next
#   def initialize(val)
#     @val = val
#     @next = nil
#   end
# end

# Definition for a binary tree node.
# class TreeNode
#   attr_accessor :val, :left, :right
#   def initialize(val)
#     @val = val
#     @left, @right = nil, nil
#   end
# end

# @param {ListNode} head
# @return {TreeNode}
def sorted_list_to_bst(head)
  return nil if head.nil?
  return TreeNode.new(head.val) if head.next.nil?

  mid = find_mid_list(head)
  root = TreeNode.new(mid.val)
  l, r = head, mid.next
  
  root.left, root.right = sorted_list_to_bst(l), sorted_list_to_bst(r)
  
  root
end

def find_mid_list(head)
  prev, slow, fast = nil, head, head

  while fast && fast.next
    prev, slow, fast = slow, slow.next, fast.next.next
  end

  # set prev pointer to nil to end the list there
  prev.next = nil

  slow
end