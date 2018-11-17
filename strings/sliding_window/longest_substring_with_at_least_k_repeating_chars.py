# Approach 1: Divide and conquer

# 1.a. recursive
# 1. Keep a set to store all characters whose frequency is less than k.
# 2. Whenever we encounter a character in this set we call the function recursively to find the longest substring with atleast k repeating characters.
# 3. Exit condition from recursion is when set for that substring is empty meaning all the characters have frequency atleast k.
# 4. At the end one more check is required in case of test case like this cababb and k = 2 
# 5. Source taken from ProgramCreek https://www.programcreek.com/2014/09/leetcode-longest-substring-with-at-least-k-repeating-characters-java/

class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0

        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))

        return len(s)

# iterative
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        stack = []
        stack.append(s)
        ans = 0

        while stack:
            s = stack.pop()

            for c in set(s):
                if s.count(c) < k:
                    stack.extend([z for z in s.split(c)])
                    break
            else:
                ans = max(ans, len(s))
        return ans

# Sliding window
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0

        mydict, myset = {}, set()

        for c in s:
            if c in mydict.keys():
                mydict[c] += 1
            else:
                mydict[c] = 1

            if mydict[c] >= k:
                myset.discard(c)
            else:
                myset.add(c)

        if len(myset) == 0:
            return len(s)

        intervals, start = [], 0
        while start < len(s):
            if s[start] not in myset:
                i = start
                while start < len(s):
                    if s[start] not in myset:
                        start += 1
                    else:
                        break 
                intervals.append((i, start))
            else:
                start += 1

        gMax = 0
        for interval in intervals:
            gMax = max(gMax, self.longestSubstring(s[interval[0]:interval[1]], k))

        return gMax

# Approach 1: A simple improvement on the naive quaratic solution. The idea is that if a locally longest substr is found, there's no need to check substrs overlapping it.
# Sol1 can run O(n) times in some cases, but worst case is O(n2). Anyway the C++ run time is 3ms.


