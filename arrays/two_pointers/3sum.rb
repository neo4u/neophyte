# @param {Integer[]} nums
# @return {Integer[][]}
def three_sum(nums)
  nums.sort!
  result = []

  0.upto(nums.length - 1) do |i|
    next if i > 0 && nums[i] == nums[i - 1]               # Skip dups
    l, r = i + 1, nums.length - 1

    while l < r
      sum = nums[i] + nums[l] + nums[r]
      if sum.zero?
        result.push([nums[i], nums[l], nums[r]])
        while l < r && nums[l += 1] == nums[l - 1] do end # Skip dups
        while l < r && nums[r -= 1] == nums[r + 1] do end # Skip dups
      elsif sum < 0
        l += 1
      elsif sum > 0
        r -= 1
      end
    end
  end

  result
end

# 15. 3Sum
# https://leetcode.com/problems/3sum/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2],[-1, 0, 1]])
