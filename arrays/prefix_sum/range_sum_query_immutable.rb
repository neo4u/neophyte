class NumArray
    def initialize(nums)
        n = nums.size
        @sum = Array.new(n + 1, 0)
        1.upto(n) { |i| @sum[i] = @sum[i - 1] + nums[i - 1] } # Calculate cumulative sum
    end

    def sum_range(i, j)
        @sum[j + 1] - @sum[i]
    end
end

# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/description/

# Approach 1: Cumulative Sum
# Steps:
# 1. Make prefix sum / cumulative sum array
#    Where sum[i] represents sum of nums sub-array of length i (nums[0 to i - 1])
#    Base case:             sum[0] = 0
#    Recurrance relation:   sum[i] = sum[i - 1] + nums[i - 1]
#    for i from 1 to n (get the sum from previous element + current element)
# 2. When sum_range(i, j) is called we subtract the cumulative sum
#    of the first idx from the idx outside the window
#    Example:[1,2,3,4, 5]
#    cum_sum:[0,1,3,6,10,15]
#    sum_range(1, 3): we need the sum 2+3+4 = 9
#    cum_sum[4] - cum[1] = 10 - 1 = 9

