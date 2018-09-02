# @param {Integer[]} preorder
# @return {Boolean}
def verify_preorder(preorder)
  stack = []
  last_inorder_num = -Float::INFINITY

  # Iterate through sequence
  preorder.each do |num|
    # This condition means
    return false if num < last_inorder_num

    # Keep popping until you find a num > top of stack
    last_inorder_num = stack.pop() while !stack.empty? && stack.last() <= num

    # Push the current num onto the stack
    stack << num
  end

  true
end

# O(n2)
# @param {Integer[]} preorder
# @return {Boolean}
def verify_preorder_alternative(preorder, l = nil, r = nil, min = -Float::INFINITY, max = Float::INFINITY)
  l, r = 0, preorder.size() - 1  if l.nil? || r.nil?

  root = preorder[l]
  return true if l > r
  return false if root > max || root < min

  rightIdx = l
  rightIdx += 1 while rightIdx <= r && preorder[rightIdx] <= root

  verify_preorder_alternative(preorder, l + 1, rightIdx - 1, min, root) &&
  verify_preorder_alternative(preorder, rightIdx, r, root, max)
end


# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/
# 255. Verify Preorder Sequence in Binary Search Tree

# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
# You may assume each number in the sequence is unique.
# Consider the following binary search tree: 
#      5
#     / \
#    2   6
#   / \
#  1   3

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(verify_preorder([40, 30, 35, 20, 80, 100]), false)
assert_equal(verify_preorder([5,2,6,1,3]), false)
assert_equal(verify_preorder([5,2,1,3,6]), true)
assert_equal(verify_preorder([45, 25, 15, 35, 75]), true)
assert_equal(verify_preorder( [30, 20, 10, 40, 50]), true)

assert_equal(verify_preorder_alternative([40, 30, 35, 20, 80, 100]), false)
assert_equal(verify_preorder_alternative([5,2,6,1,3]), false)
assert_equal(verify_preorder_alternative([5,2,1,3,6]), true)
assert_equal(verify_preorder_alternative([45, 25, 15, 35, 75]), true)
assert_equal(verify_preorder_alternative( [30, 20, 10, 40, 50]), true)