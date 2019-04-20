def three_sum(nums)
    nums.sort!
    n, result = nums.size, []
    0.upto(n - 3) do |i|
        next if i > 0 && nums[i] == nums[i - 1]     # skip dups from left
        l, r = i + 1, n - 1
        while l < r
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0
                result.push([nums[i], nums[l], nums[r]])
                l += 1; r -= 1
                l += 1 while nums[l] == nums[l - 1] # Skip dups from left
                r -= 1 while nums[r] == nums[r + 1] # Skip dups from right
            elsif sum < 0                           # Move left pointer
                l += 1
            elsif sum > 0                           # Move right pointer
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
