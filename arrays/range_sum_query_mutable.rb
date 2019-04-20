class NumArray
    def initialize(nums)
        @nums = nums
        n = @nums.size
        @sum = Array.new(n + 1, 0)
        1.upto(n) { |i| @sum[i] = @sum[i - 1] + @nums[i - 1] } # Calculate cumulative sum
    end

    def sum_range(i, j)
        @sum[j + 1] - @sum[i]
    end

    def update(i, val)
        delta = val - @nums[i]
        @nums[i] = val
        (i + 1).upto(@nums.size) { |j| @sum[j] = @sum[j] + delta }
    end
end

# Your NumArray object will be instantiated and called as such:
# obj = NumArray.new(nums)
# obj.update(i,val)
# param_2 = obj.sum_range(i,j)

# Approach 1: Brute-Force (TLE)
# Approach 2: Cumulative Sum
# Approach 3: Squre Root Composition
# Approach 4: Segment Tree

# 307. Range Sum Query - Mutable
# https://leetcode.com/problems/range-sum-query-mutable/description/

require 'test/unit'
extend Test::Unit::Assertions


arr = NumArray.new([1, 3, 5])
assert_equal(arr.sum_range(0,2), 9)
arr.update(1, 2)
assert_equal(arr.sum_range(0,2), 8)

arr = NumArray.new([7,2,7,2,0])
arr.update(4,6)
arr.update(0,2)
arr.update(0,9)
assert_equal(arr.sum_range(4,4), 6)
arr.update(3,8)
assert_equal(arr.sum_range(0,4), 32)
arr.update(4,1)
assert_equal(arr.sum_range(0,3), 26)
assert_equal(arr.sum_range(0,4), 27)
arr.update(0,4)
