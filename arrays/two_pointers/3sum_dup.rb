# @param {Integer[]} nums
# @return {Integer[][]}
def three_sum(nums)
  nums.sort!
  res, n = [], nums.length

  0.upto(n - 3) do |i|
    next if i > 0 && nums[i - 1] === nums[i] # Skip duplicates
    l, r = i + 1, n - 1

    while l < r
      s = nums[i] + nums[l] + nums[r]
      if s.zero?
				res.push([nums[i], nums[l], nums[r]])
        while l < r && nums[l += 1] == nums[l - 1] do end
        while l < r && nums[r -= 1] == nums[r + 1] do end
      elsif s < 0
        l += 1
      elsif s > 0
        r -= 1
      end
    end
  end

  res
end

# Steps
# 1. Sort the array
# 2. loop through the elements 1 by 1
# 3. After fixing 1 element use 2 pointers to navigate
#    left or right based on comparisons with the target
# 4. 

# 15. 3Sum
# https://leetcode.com/problems/3sum/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2],[-1, 0, 1]])