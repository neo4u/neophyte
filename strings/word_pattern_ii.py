class Solution:
    def wordPatternMatch(self, p: str, s: str) -> bool:
        self.bt(p, s, 0, 0, {}, {})

    def bt(self, patt, str_, i, j, p_hash, w_hash):
        m, n = len(patt), len(str_)
        if i == m and j == n: return True
        if i == m or j == n: return False

        p, mapped_this_iter = patt[i], False
        for k in range(j, n):
            w = str_[j:k + 1]
            # Test is using the word violates the rules learned thus far!
            if (p in p_hash and p_hash[p] != w) or (w in w_hash and w_hash[w] != p): continue
            # Either the rules are already learned or they need to be added.
            # added variable ensures we only remove from dictionary when we had previously added.
            if p not in p_hash and w not in w_hash: p_hash[p], w_hash[w], mapped_this_iter = w, p, True
            remainder = self.bt(patt, str_, i + 1, k + 1, p_hash, w_hash)
            if mapped_this_iter: del p_hash[p]; del w_hash[w]
            if remainder: return True

        return False



# 291. Word Pattern II
# https://leetcode.com/problems/word-pattern-ii/


# Approach from java example:
# https://leetcode.com/problems/word-pattern-ii/discuss/73664/Share-my-Java-backtracking-solution

# We can solve this problem using backtracking,
# we just have to keep trying to use a character in the pattern to
# match different length of substrings in the input string,
# keep trying till we go through the input string and the pattern.

# For example, input string is "redblueredblue", and the pattern is "abab",
# first let's use 'a' to match "r", 'b' to match "e",
# then we find that the 2nd 'a' doesn't match "d",
# so we backtrack, use 'b' to match "ed", so on and so forth ...
# When we do the recursion, if the pattern character exists in the hash map already,
# we just have to see if we can use it to match the same length of the string.

# For example, let's say we have the following map:
# 'a': "red"
# 'b': "blue"
# now when we see 'a' again, we know that it should match "red",
# the length is 3, then let's see if str[i ... i+3] matches 'a',
# where i is the current index of the input string. Or use starts_with
# Also, we can use a hash set to avoid duplicate matches,
# if char 'a' matches string "red", then character b cannot be used to match "red".
# In my opinion though, we can say apple (pattern 'a') is "fruit",
# orange (pattern 'o') is "fruit", so they can match the same string,
# anyhow, I guess it really depends on how the problem states.
# The following code should pass OJ now, if we don't need to worry about the duplicate matches,
# just remove the code that associates with the hash set.

# Backtracking solution
# 1. We divide the sub-problem as self.helper(pattern, str, i, j) to
#    answer if str[j:] follows the same pattern[i:].
# You need to be careful in the backtracking part where you delete ptable and stable.
# 2. There are two conditions when you proceed with the recursion:
#    when both ptable and stable have the right mapping and when both are empty.
#    In the latter instance, you add the mapping, therefore,
#    you delete only when under those circumstances.
#    Otherwise you can end up with an error.