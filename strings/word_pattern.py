class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        if len(pattern) != len(words): return False

        p_hash, w_hash = {}, {}
        for p, w in zip(pattern, words):
            if (p in p_hash and p_hash[p] != w) or (w in w_hash and w_hash[w] != p): return False
            p_hash[p], w_hash[w] = w, p
        return True

# abba cat dog dog fish
# pcache     wcache

# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/

# Approach 1:
# 1. Bijection between pattern and str implies that if at index i we have (pattern[i],
#    str1[i]), then at any index j (j>i), if pattern[j] == pattern[i],
#    then str1[j] must be equal to str1[i]. Similarly, if str1[j] == str1[i],
#    then pattern[j] must be same as pattern[i].
# 2. In other words, the two way mapping implied at an index must be honored for all later indicies
# 3. First thing to test is the length of the pattern and str. If they are not same, return False.
# 4. Every character in the pattern must match to a unique word in str.
#    Similarly, every word must match to a unique character in the
#    pattern - this is easy to implement using two dictionaries or hashmaps.

# Approach 2:
# We can optimize space usage by constructing hash-maps which map strings to indices which are integers.
