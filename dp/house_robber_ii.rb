# @param {Integer[]} nums
# @return {Integer}
def rob(nums)
  return 0 if nums.empty?
  return nums.max if nums.size <= 2
  [rob_seq(nums[0, nums.size - 1]), rob_seq(nums[1, nums.size])].max
end

def rob_seq(a)
  return 0 if a.empty?
  return a.max if a.size <= 2

  n, dp = a.size - 1, [-Float::INFINITY] * a.size
  dp[0], dp[1] = a[0], [a[0], a[1]].max

  2.upto(n) do |i|
    dp[i] = [dp[i - 1], dp[i - 2] + a[i]].max
  end

  dp[n]
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(rob([]), 0)
assert_equal(rob([0, 0, 0]), 0)
assert_equal(rob([1, 1, 1]), 2)
assert_equal(rob([1, 1]), 1)
