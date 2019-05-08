# @param {Integer[]} nums
# @return {Integer[][]}
def permute(nums)
    return [] if !nums || nums.empty?
    bt(nums)
end

def bt(nums, path = [], result = [])
    if nums.empty?
        result.push(path)
        return
    end

    0.upto(nums.size - 1) do |i|
        curr_removed = nums[0...i] + nums[i + 1...nums.size]
        bt(curr_removed, path + [nums[i]], result)
    end

    result
end

# class Solution:
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         def backtrack(first = 0):
#             # if all integers are used up
#             if first == n:  
#                 output.append(nums[:])
#             for i in range(first, n):
#                 # place i-th integer first 
#                 # in the current permutation
#                 nums[first], nums[i] = nums[i], nums[first]
#                 # use next integers to complete the permutations
#                 backtrack(first + 1)
#                 # backtrack
#                 nums[first], nums[i] = nums[i], nums[first]
        
#         n = len(nums)
#         output = []
#         backtrack()
#         return output

def permute(nums)
    return [] if !nums || nums.empty?
    bt(nums)
end

def bt(nums, first = 0, results = [])
    results.push(nums.dup) if first == n

    first.upto(nums.size - 1) do |i|
        nums[first], nums[i] = nums[i], nums[first]
        bt(nums, first + 1, results)
        nums[first], nums[i] = nums[i], nums[first]
    end

    results
end



# bt(0, [1 2 3])
#     bt(1, [1,2,3])
#         bt(2, [1,2,3])
#         ret
#         bt(2, [1,3,2])
#         ret
#     bt(1, [2,1,3])
#         bt(2, [2,1,3])
#         bt(2, [2,3,1])
#     bt(1, [3,2,1])
#         bt(2, [3,2,1])
#         bt(2, [3,1,2])



# 46. Permutations
# https://leetcode.com/problems/permutations/description/

# Example: nums = [1,2,3]
# dfs call nums: [1, 2, 3] | path: [] | result: []
#     dfs call nums: [2, 3] | path: [1] | result: []
#         dfs call nums: [3] | path: [1, 2] | result: []
#             dfs call nums: [] | path: [1, 2, 3] | result: []
#         dfs retn nums: [3] | path: [1, 2] | result: [[1, 2, 3]]
#         dfs call nums: [2] | path: [1, 3] | result: [[1, 2, 3]]
#             dfs call nums: [] | path: [1, 3, 2] | result: [[1, 2, 3]]
#         dfs retn nums: [2] | path: [1, 3] | result: [[1, 2, 3], [1, 3, 2]]
#     dfs retn nums: [2, 3] | path: [1] | result: [[1, 2, 3], [1, 3, 2]]
#     dfs call nums: [1, 3] | path: [2] | result: [[1, 2, 3], [1, 3, 2]]
#         dfs call nums: [3] | path: [2, 1] | result: [[1, 2, 3], [1, 3, 2]]
#             dfs call nums: [] | path: [2, 1, 3] | result: [[1, 2, 3], [1, 3, 2]]
#         dfs retn nums: [3] | path: [2, 1] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3]]
#         dfs call nums: [1] | path: [2, 3] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3]]
#             dfs call nums: [] | path: [2, 3, 1] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3]]
#         dfs retn nums: [1] | path: [2, 3] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]]
#     dfs retn nums: [1, 3] | path: [2] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]]
#     dfs call nums: [1, 2] | path: [3] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]]
#         dfs call nums: [2] | path: [3, 1] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]]
#             dfs call nums: [] | path: [3, 1, 2] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]]
#         dfs retn nums: [2] | path: [3, 1] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]]
#         dfs call nums: [1] | path: [3, 2] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]]
#             dfs call nums: [] | path: [3, 2, 1] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]]
#         dfs retn nums: [1] | path: [3, 2] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
#     dfs retn nums: [1, 2] | path: [3] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# dfs retn nums: [1, 2, 3] | path: [] | result: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(permute([1,2,3]), [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
])

