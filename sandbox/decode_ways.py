class Solution:
    def numDecodings(self, s: str):
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1

        for i in range(2, n + 1):
            d1 = int(s[i - 1])
            if 1 <= d1 <= 9:
                dp[i] = dp[i - 1]

            d2 = int(s[i - 2 : i])
            if 10 <= d2 <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/description/