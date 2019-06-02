class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [0 for _ in xrange(N + 1)]
        dp[0] = 1
        for i in xrange(1, N+1):
            if i <= K:
                # sliding window. size = W
                dp[i] = sum(dp[max([i - W, 0]):i]) * 1.0 / W
            else:
                # start from dp[m] where m < K, and take one more step to i. i>K.
                dp[i] = sum(dp[max([i - W, 0]):K]) * 1.0 / W
        res = sum(dp[K:])
        return res


# 837. New 21 Game
# https://leetcode.com/problems/new-21-game/description/

# dp[i] represents the total probability to get points i
# dp[i] = dp[1] * 1/W + dp[2] * 1/W + dp[3] * 1/W + ... dp[i-2] * 1/W + dp[i-1] * 1/W
# So dp[i] = (dp[1] + dp[2] + ... + dp[i - 1]) / W = Wsum / W

# Conditional probability: keep a window with size K (assume K = 10), the probability of getting point i is the sum
# of probability from point i - 10 to i, point i - 9 to i, ... , i -1 to i. Since every card has equal probability,
# the probability to get any one of cards is 1/10. So the total probability of dp[i] is sum of all conditional
# probability.
# Once i is over than or equal to K, we can accumulate probability to final result