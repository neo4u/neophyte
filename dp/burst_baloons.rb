# @param {Integer[]} nums
# @return {Integer}
def max_coins(nums)
    nums.unshift(1) << 1 # Insert a 1 at the start and end unshift adds at start, << adds at the end
    n = nums.size
    dp = Array.new(n) { Array.new(n, 0) }

    2.upto(n) do |sub_array_size|         # Consider all array from size 2 to n - 1
        0.upto(n - sub_array_size - 1) do |l| # l will vary from 0 to n - k - 1
            r = l + sub_array_size            # l to r will always be of length k
            (l + 1).upto(r - 1) do |k|
                # Keep updating the dp with the max value for this array of size k
                # for each i from left bound to right bound
                dp[l][r] = [
                    dp[l][r],
                    dp[l][k] + nums[l] * nums[k] * nums[r] + dp[k][r]
                ].max
            end
        end
    end

    # Since dp[l][r] represents max coins of obtained by bursting balloons for between l and r (inclusive)
    # therefore, dp[0][n - 1] gives us for entire nums array
    dp[0][n - 1]
end


# 312. Burst Balloons
# https://leetcode.com/problems/burst-balloons/description/

# Time: O(n^3)
# Space O(n^2)

# Explanation summarized from below compilation of explanations
# for l and r that vary between 0 and n - 1
# for k from l to r
# dp[l][r] = max | dp[l][r]
#                | nums[l] * nums[k] * nums[r] +    dp[l][k]     + dp[k][r])
#                         burst k             | burstt left of k | burst right of k

#                       l - 1, l, l + 1, ... , k - 1, k, k + 1, ..., r - 1, r, r + 1
#                              ---------------------     --------------------
#                                     dp[l][k]            dp[k][r]
# This essentially means consider every sub-array (sub array sizes 1 to n)
#   for the sub-array consider every possible position of k between l and r (bounds of the sub-array)
#   and see the maximum coins possible for that sub-array
# keep using the smaller sub-array values to calculate the values for bigger sub-arrays.



# BEST EXPLANATION FROM LEETCODE
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
# When I first get this problem, it is far from dynamic programming to me.
# I started with the most naive idea the backtracking.
# We have n balloons to burst, which mean we have n steps in the game.
# In the i th step we have n-i balloons to burst, i = 0~n-1.
# Therefore we are looking at an algorithm of O(n!).
# Well, it is slow, probably works for n < 12 only.
# Of course this is not the point to implement it.
# We need to identify the redundant works we did in it and try to optimize.
# Well, we can find that for any balloons left the
# maxCoins does not depends on the balloons already bursted.
# This indicate that we can use memorization (top down) or dynamic programming (bottom up)
# for all the cases from small numbers of balloon until n balloons.
# How many cases are there? For k balloons there are C(n, k) cases and
# for each case it need to scan the k balloons to compare. The sum is quite big still.
# It is better than O(n!) but worse than O(2^n).

# Better idea
# We then think can we apply the divide and conquer technique? 
# After all there seems to be many self similar sub problems from the previous analysis.
# Well, the nature way to divide the problem is burst one balloon and
# separate the balloons into 2 sub sections one on the left and one one the right.
# However, in this problem the left and right become adjacent and have effects on the maxCoins in the future.
# Then another interesting idea come up. Which is quite often seen in dp problem analysis.
# That is reverse thinking. Like I said the coins you get for a balloon does not depend on the balloons already burst.
# Therefore instead of divide the problem by the first balloon to burst,
# we divide the problem by the last balloon to burst.
# Why is that? Because only the first and last balloons we are sure of their adjacent balloons before hand!

# For the first we have nums[i-1]*nums[i]*nums[i+1] for the last we have nums[-1]*nums[i]*nums[n].
# OK. Think about n balloons if i is the last one to burst, what now?
# We can see that the balloons is again separated into 2 sections.
# But this time since the balloon i is the last balloon of all to burst,
# the left and right section now has well defined boundary and do not affect each other!
# Therefore we can do either recursive method with memoization or dp.

# Final
# Here comes the final solutions.
# Note that we put 2 balloons with 1 as boundaries and
# also burst all the zero balloons in the first round since they won't give any coins.
# The algorithm runs in O(n^3) which can be easily seen from the 3 loops in dp solution.


# I think the most upvoted post didn't talk about what dp[i][j] represent and what exactly does the transition function :


# Or maybe it did talk about it but I miss it.
# But anyway here is my understand of this problem after reading countless of posts and comments:
# First of all, dp[i][j] in here means,
# the maximum coins we get after we burst all the balloons between i and j in the original array.
# For example with input [3,1,5,8] :
# dp[0][0] means we burst ballons between [0,0],
# which means we only burst the first balloon in original array. So dp[0][0] is 1 * 3 * 1 = 3.
# dp[1][1] means we burst balloons between [1][1],
# which means we only burst the second ballon in the original array. So dp[1][1] is 3 * 1 * 5 = 15.

# So in the end for this problem we want to find out dp[0][ arr.length - 1 ], which is the maximum value we can get when we burst all the balloon between [0 , length -1]

# To get that we need the transition function :

# for (int k = left; k <= right; ++k)
# dp[left][right] = max(dp[left][right], nums[left-1] * nums[k] * nums[right+1] + dp[left][k-1] + dp[k+1][right])**

# This transition function basically says: 
# in order to get the maximum value we can get for bursting all the balloons between [i,j],
# we just loop through each balloon between these two indexes and make them to be the last balloon to be burst,
# why we pick it as the last balloon to burst ?

# For example when calculating dp[0,3] and picking index 2 as the last balloon to burst,
# [ 3 , 1 , 5 , 8], that means 5 is the last balloon to burst between [0,3],
# to get the maximum value when picking 5 as the last balloon to burst :
# max = maximum value of bursting all the balloon on the left side of 5 +
#       maximum value of bursting all the balloon on the right side of 5 +
#       bursting balloon 5 when left side and right side are gone.

# That is dp[0, 1] + nums[0 - 1] * nums[2] * nums[3 + 1] + + dp[3,3];
# That is dp[left, k - 1] + nums[left - 1] * nums[k] * nums[right + 1] + dp[k+1, right] ;
# to get the maximum dp[left, right] we just loop through all the possible value of k to get the maximum.
# Hope it helps!

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_coins([3,1,5,8]), 167)

