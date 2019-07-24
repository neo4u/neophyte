class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict, n = set(wordDict), len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_dict:
                    dp[i] = True
                    break

        return dp[n]



# 139. Word Break
# https://leetcode.com/problems/word-break/




# dp[i] = can you break the sentence from 0 to i into words in the dict
# dp[i] = True if dp[j] = True and s[j+1:i] is in the dict for every j from 0 to i-1
# dp[0] = True , empty string is in the dict
