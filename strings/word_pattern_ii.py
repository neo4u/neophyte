
class Solution:
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.dfs(pattern, str, {})

    def dfs(self, pattern, str, dict):
        if len(pattern) == 0 and len(str) > 0:
            return False
        if len(pattern) == len(str) == 0:
            return True
        for end in range(1, len(str)-len(pattern)+2): # +2 because it is the "end of an end"
            if pattern[0] not in dict and str[:end] not in dict.values():
                dict[pattern[0]] = str[:end]
                if self.dfs(pattern[1:], str[end:], dict):
                    return True
                del dict[pattern[0]]
            elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
                if self.dfs(pattern[1:], str[end:], dict):
                    return True
        return False


# 291. Word Pattern II
# https://leetcode.com/problems/word-pattern-ii/


# Approach from java example:
# https://leetcode.com/problems/word-pattern-ii/discuss/73664/Share-my-Java-backtracking-solution

# We can solve this problem using backtracking, we just have to keep trying to use a character in the pattern to match different length of substrings in the input string, keep trying till we go through the input string and the pattern.
# For example, input string is "redblueredblue", and the pattern is "abab", first let's use 'a' to match "r", 'b' to match "e", then we find that 'a' does not match "d", so we do backtracking, use 'b' to match "ed", so on and so forth ...
# When we do the recursion, if the pattern character exists in the hash map already, we just have to see if we can use it to match the same length of the string. For example, let's say we have the following map:
# 'a': "red"
# 'b': "blue"
# now when we see 'a' again, we know that it should match "red", the length is 3, then let's see if str[i ... i+3] matches 'a', where i is the current index of the input string. Thanks to StefanPochmann's suggestion, in Java we can elegantly use str.startsWith(s, i) to do the check.
# Also thanks to i-tikhonov's suggestion, we can use a hash set to avoid duplicate matches, if character a matches string "red", then character b cannot be used to match "red". In my opinion though, we can say apple (pattern 'a') is "fruit", orange (pattern 'o') is "fruit", so they can match the same string, anyhow, I guess it really depends on how the problem states.
# The following code should pass OJ now, if we don't need to worry about the duplicate matches, just remove the code that associates with the hash set.

# Approach from python example:
# Use dictionary to store patterns, and backtrack when mismatch happens.
