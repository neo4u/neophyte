# @param {Integer[]} nums
# @return {Integer}
def array_pair_sum(nums)
    nums, sum = nums.sort, 0
    nums.each_slice(2) do |a1, _|
        sum += a1
    end

    sum
end


# 561. Array Partition I
# https://leetcode.com/problems/array-partition-i/description/