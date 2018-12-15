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

