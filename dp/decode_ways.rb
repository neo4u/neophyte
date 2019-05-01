# @param {String} s
# @return {Integer}
def num_decodings(s)
    return 0 if !s || s.empty?
    n = s.size
    dp = Array.new(n + 1, 0)
    dp[0] = 1
    dp[1] = s[0] != '0' ? 1 : 0

    2.upto(n) do |i|
        # if current char is a number other than zero, then add way to decode from dp[i - 1].
        # consider "1234" if we're at '4', its a non-zero char,
        # thus the curr value '4' adds to the same decoding of '123' as 'abc'
        # and forms 'abcd' which is one encoding of '1234'
        # Also we can make this condition as s[i - 1] != '0',
        # which means the same thing as between '1', '9', whitelist vs blacklist kinda thing
        dp[i] += dp[i - 1] if s[i - 1].between?('1', '9')

        # Continuing the '1234' example we're at '4', given that '34' is not between '10' and '26'
        # we don't add any new decoding ways by adding 4.
        # However, if we're using '1224' and we were at '4' then '24' has a mapping and hence we add
        # dp[i - 2] which is ways of decoding '12' to the current number of ways
        dp[i] += dp[i - 2] if s[i - 2...i].between?('10', '26') # s[i - 2...i] gives the current char along with the previous char
    end

    dp[n]
end

# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

# dp[i] represents the number of ways to decode string of length i
# dp[0] represents ways to decode string of length 0 [This is key, and we need to make this 1,
#                                                     for this entire thing to work!!
#                                                     Although it doesn't make sense
#                                                     for decoding empty string in 1 way]
# dp[1] represents ways to decode string of length 1 and so on...

# Now we want number of ways to decode s (length n),
# so we require dp[n], which represents ways to decode string of length n.

# 2 conditions
# 1. We have curr char between '1' and '9' (non-zero),
#    we just use previous number of decodings for upto length i - 1
# 2. We have the combo of curr and prev char are between '10', '26'
#    then we add ways to encode of upto i - 2 to the curr value

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