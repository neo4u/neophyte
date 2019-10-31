# @param {Integer[]} nums
# @return {Integer}
def rob(nums)
    return 0 if nums.empty?
    return nums.max if nums.size <= 2

    [rob_seq(nums[0, nums.size - 1]), rob_seq(nums[1, nums.size])].max
end

def rob_seq(nums)
    return 0 if nums.empty?
    return nums.max if nums.size <= 2

    n = nums.size
    dp = [-1] * n
    dp[0], dp[1] = nums[0], [nums[0], nums[1]].max

    2.upto(n - 1) do |i|
        dp[i] = [dp[i - 1], dp[i - 2] + nums[i]].max
    end

    dp[n - 1]
end
