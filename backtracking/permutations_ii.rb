# @param {Integer[]} nums
# @return {Integer[][]}
def permute_unique(nums)
    return [] if !nums || nums.empty?
    nums.sort!()
    bt(nums)
end

def bt(nums, path = [], result = [])
    if nums.empty?
        result.push(path)
        return
    end

    0.upto(nums.size - 1) do |i|
        next if i > 0 && nums[i] == nums[i - 1] # Skip duplicates, after i crosses 0
        nums_with_curr_removed = nums[0...i] + nums[i + 1...nums.size]
        bt(nums_with_curr_removed, path + [nums[i]], result)
    end

    result
end

# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(permute_unique([1,1,2]), [
    [1,1,2],
    [1,2,1],
    [2,1,1]
])
assert_equal(permute_unique([1,2,2,4]), [
    [1,2,2,4],
    [1,2,4,2],
    [1,4,2,2],
    [2,1,2,4],
    [2,1,4,2],
    [2,2,1,4],
    [2,2,4,1],
    [2,4,1,2],
    [2,4,2,1],
    [4,1,2,2],
    [4,2,1,2],
    [4,2,2,1]
])

