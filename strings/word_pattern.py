class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        if len(pattern) != len(words):
            return False
        pcache, wcache = {}, {}
        for p, w in zip(pattern, words):
            if (p in pcache and pcache[p] != w) or (w in wcache and wcache[w] != p):
                return False
            pcache[p], wcache[w] = w, p
        return True

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        if len(pattern) != len(words):
            return False
        pcache, wcache = {}, {}
        for idx, (p, w) in enumerate(zip(pattern, words)):
            if p in pcache:
                if w not in wcache or pcache[p] != wcache[w]:
                    return False
            else:
                pcache[p] = idx
            if w in wcache:
                if p not in pcache or wcache[w] != pcache[p]:
                    return False
            else:
                wcache[w] = idx
        return True

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
