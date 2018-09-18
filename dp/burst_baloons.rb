# @param {Integer[]} nums
# @return {Integer}
def max_coins(nums)
    nums.unshift(1) << 1
    n = nums.size
    dp = Array.new(n) { Array.new(n, 0) }

    2.upto(n - 1) do |k|         # Consider all array from size 2 to n - 1
        0.upto(n - k - 1) do |l| # l will vary from 0 to n - k - 1
            r = l + k            # l to r will always be of length k
            (l + 1).upto(r - 1) do |i|
                # Keep updating the dp with the max value for this array of size k
                dp[l][r] = [
                    dp[l][r],
                    dp[l][i] + nums[l] * nums[i] * nums[r] + dp[i][r]
                ].max
            end
        end
    end

    # Since dp[i][j] represents max coins of array nums[i to j] dp[0][n - 1] gives us for nums
    dp[0][n - 1]
end


# 312. Burst Balloons
# https://leetcode.com/problems/burst-balloons/description/

# Time: O(n**3)
# Space O(n**2)

# 1. define subproblems
# dp[i][j] : the maximum coins we can collect by bursting all the balloons in nums[i:j+1]
# number of subproblems O(N**2)
# 2. guess
# What is the last balloon to burst in nums[i:j+1]
# number of choices o(j - i + 1) or o(N)
# 3. relate subproblem solutions
# i - 1, i, i + 1, ... , k - 1, k, k + 1, ..., j - 1, j, j + 1
#        ---------------------     --------------------
#               dp[i][k - 1]            dp[k + 1][j]
              
# dp[i][j] = max(dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j])  i <= k <= j
# corner case: i == k == j, dp[i][i - 1] and dp[k + 1][j] initialized to zero --> same equation
# time per subproblem o(j - i) or O(N)
# 4. topological order
# length from 1 to n
# 5. original problem
# 1, X, ..., X    , X, 1      nums
# 0, 1, ..., n - 1, n, n + 1  index
#    ----------------
#       dp[1][n]

#       def maxCoins(self, iNums):


# Be Naive First
# When I first get this problem, it is far from dynamic programming to me. I started with the most naive idea the backtracking.
# We have n balloons to burst, which mean we have n steps in the game. In the i th step we have n-i balloons to burst, i = 0~n-1. Therefore we are looking at an algorithm of O(n!). Well, it is slow, probably works for n < 12 only.
# Of course this is not the point to implement it. We need to identify the redundant works we did in it and try to optimize.
# Well, we can find that for any balloons left the maxCoins does not depends on the balloons already bursted. This indicate that we can use memorization (top down) or dynamic programming (bottom up) for all the cases from small numbers of balloon until n balloons. How many cases are there? For k balloons there are C(n, k) cases and for each case it need to scan the k balloons to compare. The sum is quite big still. It is better than O(n!) but worse than O(2^n).

# Better idea
# We then think can we apply the divide and conquer technique? After all there seems to be many self similar sub problems from the previous analysis.
# Well, the nature way to divide the problem is burst one balloon and separate the balloons into 2 sub sections one on the left and one one the right. However, in this problem the left and right become adjacent and have effects on the maxCoins in the future.
# Then another interesting idea come up. Which is quite often seen in dp problem analysis. That is reverse thinking. Like I said the coins you get for a balloon does not depend on the balloons already burst. Therefore
# instead of divide the problem by the first balloon to burst, we divide the problem by the last balloon to burst.
# Why is that? Because only the first and last balloons we are sure of their adjacent balloons before hand!

# For the first we have nums[i-1]*nums[i]*nums[i+1] for the last we have nums[-1]*nums[i]*nums[n].
# OK. Think about n balloons if i is the last one to burst, what now?
# We can see that the balloons is again separated into 2 sections. But this time since the balloon i is the last balloon of all to burst, the left and right section now has well defined boundary and do not affect each other! Therefore we can do either recursive method with memoization or dp.

# Final
# Here comes the final solutions. Note that we put 2 balloons with 1 as boundaries and also burst all the zero balloons in the first round since they won't give any coins.
# The algorithm runs in O(n^3) which can be easily seen from the 3 loops in dp solution.

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_coins([3,1,5,8]), 167)

