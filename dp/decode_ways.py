class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        if s[0] != '0': dp[1] = 1

        for i in range(2, n + 1):
            d1, d2 = int(s[i - 1]), int(s[i - 2:i])

            if 1 <= d1 <= 9: dp[i] = dp[i - 1]
            if 10 <= d2 <= 26: dp[i] += dp[i - 2]

        return dp[n]


# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

# Intuition:
# dp[i] represents the number of ways to decode string of length i
# dp[0] represents ways to decode string of length 0
#       ***This is key, and we need to make this 1, for this entire thing to work***
#       cuz Empty int maps to empty string or first 0 chars represent '', so 1 mapping**
# dp[1] represents ways to decode string of len 1. We can't have 0 as the char,
#       hence we use dp[1] = 1 only if s[0] != '0'

# Hence, Base Case:
# dp[0] = 1
# dp[1] = 1 if s[0] != '0'

# Recurrance
# dp[i] number of ways to decode first i chars of s

# Recurrance Relation:
# dp[i] = (+ dp[i - 1] if s[i - 1] is between 1 between 9 )
#         (+ dp[i - 2] if s[i-2:i] is between 10 and 26)

# Goal:
# 1.Now we want number of ways to decode s (length n),
# so we require dp[n], which represents ways to decode string of length n.

# 2 conditions
# 1. We have curr char between '1' and '9' (non-zero),
#    we just use previous number of decodings for upto length i - 1,
#    meaning that the decoding for s[i] gets added to every encoding so far, so we just use dp[i - 1]
# 2. We have the combo of curr and prev char are between '10', '26'
#    then we add ways to encode of upto i - 2 to the curr value
#    meaning that the decoding for s[i - 2:i] get added to every encoding so far, for dp[i - 2]
#    so we do a dp[i] += cuz we want to add to the encodings of for 1 char and 3 chars

# Example: "123"
# Ways to decode = 3; 1 2 3, 12 3, 1 23
# dp = [1, 1, 0, 0]
# i: 2, need to find: dp[2], we need to check:
# s[i - 1] = s[1] = "2", s[i-2 to i - 1] = s[0 to 1] = "12", both have mappings so add both
#             |
#             v
# dp = [1, 1, 1 + 1, 0]

# i: 3, need to find: dp[3], we need to check:
# s[i - 1] = s[2] = "3", s[i-2 to i - 1] = s[1 to 2] = "23", both have mappings so add both
#                |
#                v
# dp [1, 1, 2, 2 + 1]
# Finally, answer is dp[n]
# 3 ways to decode

# Time: O(n)
# Space: O(n)
