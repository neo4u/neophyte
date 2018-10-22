# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
    while m > 0 && n > 0
        if nums1[m - 1] > nums2[n - 1]
            nums1[m + n - 1] = nums1[m - 1] # Copy nums1 element as it is the max element
            m -= 1                          # Move nums1's last index to left
        else
            nums1[m + n - 1] = nums2[n - 1] # Copy nums2 element as it is the max element
            n -= 1                          # Move nums2's last index to left
        end
    end
    nums1[0...n] = nums2[0...n] if n > 0

    nums1 # Comment this out for submission into leetcode. Bcuz we need in place
end


# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/


# Approach Merge Sort
# Start placing elements in their final places from the back.
# Each time we place an element from nums1's inital part to the back part
# we're freeing a position for elements to replace the front part.
# So, eventually all the elements from the front part would've been copied over to their final position
# So we're not losing any data

# Approach Merge Sort
# def merge(self, nums1, m, nums2, n):
#     while m > 0 and n > 0:
#         if nums1[m-1] >= nums2[n-1]:
#             nums1[m+n-1] = nums1[m-1]
#             m -= 1
#         else:
#             nums1[m+n-1] = nums2[n-1]
#             n -= 1
#     if n > 0:
#         nums1[:n] = nums2[:n]

# Time: O(m + n), to put simply linear
# Space: O(1)

# Demo
# Merge Two Sorted Arrays
# This is a mental model of implementing merge sort using two reader pointers and a writer pointer. The time complexity is O(M + N), while space complexity is O(1).

#   [1, 2, 5, 7, 9, 9, 0, 0, 0] # initialize pointers, W = m + n - 1
#                   R1       W  # compare R1 and R2
#      [4, 5, 8]                # R1 > R2
#             R2

#                   ┌--------┐
#   [1, 2, 5, 7, 9, 9, 0, 0, 9]
#                   R1       W  #  Write R1's value
#      [4, 5, 8]
#             R2 

#   [1, 2, 5, 7, 9, 9, 0, 0, 9]
#                R1       W     #  Move R1 and W to the left
#      [4, 5, 8]
#             R2  
#                ┌--------┐
#   [1, 2, 5, 7, 9, 9, 0, 9, 9]
#                R1       W     # R1 > R2 => Write R1's value
#      [4, 5, 8]
#             R2


#   [1, 2, 5, 7, 9, 9, 0, 9, 9]
#             R1       W     # Move R1 and W left
#      [4, 5, 8]
#             R2


#   [1, 2, 5, 7, 9, 9, 8, 9, 9]
#             R1       W     # R1 < R2 => Write R2's value
#      [4, 5, 8]       |
#             R2 ------┘   

#   [1, 2, 5, 7, 9, 9, 8, 9, 9]
#             R1    W        #  Move R2 and W to the left
#      [4, 5, 8]
#          R2
#             +-----v
#   [1, 2, 5, 7, 9, 7, 8, 9, 9]
#             R1    W        # R1 > R2 => Write R1's value
#      [4, 5, 8]
#          R2     

#   [1, 2, 5, 7, 9, 7, 8, 9, 9]
#          R1    W        # Move R1 and W to the left
#      [4, 5, 8]
#          R2

#   [1, 2, 5, 7, 5, 7, 8, 9, 9]
#          R1    W        # R1 >= R2, write R1's value
#      [4, 5, 8]
#          R2 

#   [1, 2, 5, 7, 5, 7, 8, 9, 9]
#       R1    W        # Move R1 and W to the left
#      [4, 5, 8]
#          R2 

#   [1, 2, 5, 5, 5, 7, 8, 9, 9]
#       R1    W        # R2 > R1 => Write R2's value
#      [4, 5, 8]
#          R2

#   [1, 2, 5, 5, 5, 7, 8, 9, 9]
#       R1 W        # Move R2 and W to the left
#      [4, 5, 8]
#       R2  

#   [1, 2, 4, 5, 5, 7, 8, 9, 9]
#       R1 W        # Write R2's value.
#      [4, 5, 8]
#       R2  

#       W
#   [1, 2, 4, 5, 5, 7, 8, 9, 9]
#       R1         # If R2 < 0, break loop
#      [4, 5, 8]
#   R2                                                   

# There's an edge case where R1 is less than 0, while R2 is still pointing to some value. In this case, we assume that R1's value is -INFINITY and always write R2's value:

#   [4, 0, 0, 0] # Initialize pointers
#    R1       W 
#   [1, 2, 3]
#          R2

#   [4, 0, 0, 4] # R1 >= R2, write R1's value
#    R1       W 
#   [1, 2, 3]
#          R2         

#   [4, 0, 0, 4] # Move R1 and W one index to the left
# R1       W     # R1 < 0
#   [1, 2, 3]
#          R2

#   [4, 0, 0, 4] # If R1 < 0, always write R2's value
# R1       W 
#   [1, 2, 3]
#          R2      

#   [4, 0, 3, 4] # Move W and R2 to the left and repeat
# R1    W 
#   [1, 2, 3]
#       R2           
# ...

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(merge([2, 0], 1, [1], 1), [1, 2])
assert_equal(merge([1, 2, 3, 4, 5], 5, [8, 9, 10, 11, 12, 12, 16], 7), [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 12, 16])

