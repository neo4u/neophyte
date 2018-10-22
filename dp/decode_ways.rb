# @param {String} s
# @return {Integer}
def num_decodings(s)
    return 0 if !s || s.empty?
    n = s.size
    dp = Array.new(n + 1, 0)
    dp[0] = 1
    dp[1] = s[0] != '0' ? 1 : 0

    2.upto(n) do |i|
        # if current char is a number other than zero, then add way to decode from i - 1.
        # consider "1234" if we're at '4', its a non-zero char,
        # thus the curr value '4' adds to the same decoding of '123' as 'abc'
        # and forms 'abcd' which is one encoding of '1234'
        # Also we can make this condition as s[i - 1] != '0',
        # which means the same thing as between '1', '9', whitelist vs blacklist kinda thing
        dp[i] += dp[i - 1] if s[i - 1].between?('1', '9') # Or s[i - 1...i] which is equivalent to s[i - 1] as it gives 1 char

        # Continuing the '1234' example we're at '3', and thus '34' is between '10' and '26'
        # So, we have another encoding for '123' which is taking '12' and '3' together 'LC'
        # So we're adding to an existing decoding from length i - 2, which is dp[i - 2]
        # However, if we're using '1208' and we were at '8' then 08 doesn't add another way to encode to '0'
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
#    we just use previous number of decoding for upto length i - 1
# 2. We have the combo of curr and prev char are between '10', '26'
#    then we add ways to encode of upto i - 2 to the curr value

# Time: O(n)
# Space: O(n)