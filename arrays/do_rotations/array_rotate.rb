# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate(nums, k)
    n, k, j = nums.size, k % nums.size, 0
    
    while n > 0 && k % n != 0
        0.upto(k - 1) do |i|
            nums[j + i], nums[nums.size - k + i] = nums[nums.size - k + i], nums[j + i]
        end
        n, j = n - k, j + k
        k %= n
    end
end

# Same thing using array splicing in python
# class Solution:
#     # @param nums, a list of integer
#     # @param k, num of steps
#     # @return nothing, please modify the nums list in-place.
#     def rotate(self, nums, k):
#         if not nums or not k:
#             return None

#         k %= len(nums)

#         if k:
#             nums[:k], nums[k:] = nums[-k:], nums[:-k]

# Iterative and improved solution:
# put the last k elements in correct position (ahead) and do the remaining n - k.
# Once finish swap, the n and k decrease.

# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         n, k, j = len(nums), k % len(nums), 0
#         while n > 0 and k % n != 0:
#             for i in xrange(0, k):
#                 nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i] # swap
#             n, j = n - k, j + k
#             k = k % n
# O(n) in time, O(1) in space


# All solutions in python
# https://leetcode.com/problems/rotate-array/discuss/54426/Summary-of-solutions-in-Python

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(rotate([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])
assert_equal(rotate([1,2,3,4,5], 3), [3,4,5,1,2])
