class BST
    attr_accessor :root
    class BstNode
        attr_accessor :val, :left, :right, :count, :left_tree_size
        
        def initialize(val)
            @val = val
            @left, @right = nil, nil
            @count = 1
            @left_tree_size = 0
        end
    end

    def initialize()
        @root = nil
    end

    # 1. Inserts the value in the BST
    # 2. Returns the count of values after self that are lesser than self
    def insert(val, node = nil)
        node = @root if node.nil?

        # 1: If val == node.val, count = left_tree_size.
        # 2: If val > node.val, count = left_tree_size + count + insert(val, node.right)
        # 3: If val < node.val, count = insert(val, node.left)
        if node.nil?
            @root = BstNode.new(val)
            return 0
        elsif val < node.val
            node.left_tree_size += 1                                                        # We found more value less that node.val so inc its left_tree_size for future reference, this makes no differnce for current insert
            return insert(val, node.left) if node.left                                      # If left sub-tree exists, use it to insert the val accordingly
            node.left = BstNode.new(val)                                                    # if left sub-tree was nil
            return 0                                                                        # Values less than self are 0 at this point
        elsif val > node.val
            return node.count + node.left_tree_size + insert(val, node.right) if node.right # if right sub-tree exists, use it to insert the val accordingly
            node.right = BstNode.new(val)                                                   # if right sub-tree was nil
            return node.count + node.left_tree_size                                         # we just return node count + left_tree_size as that gives the values less that val
        else                                                                                # if val == node.val
            node.count += 1                                                                 # We just increment the count of the val
            return node.left_tree_size                                                      # return left_tree_size for the curr node
        end
    end
end

# @param {Integer[]} nums
# @return {Integer[]}
def count_smaller(nums)
    tree = BST.new()
    counts, n = [], nums.size

    (n - 1).downto(0) do |i|                    # Iterate from the end and insert into tree
        counts.unshift(tree.insert(nums[i]))    # Since we're going from back insert from front of list 
    end

    counts
end


# 315. Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# Approach 1: Segment Tree
# Approach 2: Binary Indexed Tree
# Approach 3: Binary Search Tree

# Example 1: [4, 3, 2, 1]


# Approach 4: Merge-sort
# MergeSort-based solution is a standard way to solve problems related to inverse numbers.
# Here is an example to illustrate the general idea of MergeSort-based algorithm:
# Now we want to consider an array
#             6 4 1 8 7 5 2 9
# First thing first, split the array into to subarrays:
#             6 4 1 8
#             7 5 2 9
# and then calculate the inverse numbers within the group:
#                   1 4(1) 6(1,4) 8
#                   2 5(2) 7(2,5) 9
# where the numbers in the parentheses are the numbers that should be counted when we calculate the inverse number.

# Now we need to merge these two arrays into one sorted array. The first element to be put into the sorted destination array is the "1" in the first array.
#  1                  4(1) 6(1,4) 8
#                   2 5(2) 7(2,5) 9               merged elements in the 2nd array = ()

# The second element to merge is the "2" in the second array:
#  1 2                4(1) 6(1,4) 8
#                     5(2) 7(2,5) 9               merged elements in the 2nd array = (2)

# The third element to merge is the "4" in the first array:
#  1 2 4(1,2)              6(1,4) 8
#                     5(2) 7(2,5) 9               merged elements in the 2nd array = (2)

# When we merge the "4(1)", we found that "4" is actually greater than all merged elements in the second array (i.e. [2]). Therefore, we also need to consider those elements. Therefore, the numbers in the parenthese of 2 become (1)+(2) = (1,2). Next step:
#  1 2 4(1,2) 5(2)         6(1,4) 8
#                          7(2,5) 9               merged elements in the 2nd array = (2,5)

# Next (add the inverse number of element "6" by 2)
#  1 2 4(1,2) 5(2) 6(1,4,2,5)     8
#                          7(2,5) 9               merged elements in the 2nd array = (2,5)
# So and so forth, finally reach
#  1 2 4(1,2) 5(2) 6(1,4,2,5) 7(2,5) 8(2,5,7) 9
#                                                 merged elements in the 2nd array = (2,5,7,9)
# Additionally, when we need to count the inverse number, we do not need to record the exact elements, we only need to record the numbers. So, we can use a variable to record the number of "merged elements in the 2nd array" (for example, semilen in the code beneath) and the number of smaller elements of each element (for example, results[idx] in the code beneath).

# Complexity:
# Time: O(n log n)
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(count_smaller([5,2,6,1]), [2,1,1,0])
assert_equal(count_smaller([4, 3, 2, 1]), [3, 2, 1, 0])
