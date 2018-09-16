# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
    n = nums.size
    dp = [-Float::INFINITY] * n
    max = dp[0] = nums[0]

    1.upto(n - 1) do |i|
        dp[i] = [dp[i - 1] + nums[i], nums[i]].max
        max = [dp[i], max].max
    end

    max
end

nums = [-2,-1,-3,-4,-1,-2,-1,-5,-4]
# nums = [1]
puts max_sub_array(nums)
