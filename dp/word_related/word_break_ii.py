from typing import List


class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.memo = {}
        return self.dfs(s, wordDict)

    def dfs(self, s, word_dict):
        if s in self.memo: return self.memo[s]
        if not s: return []

        result = []
        for word in word_dict:
            if not s.startswith(word): continue

            if len(word) == len(s): result.append(word)
            else:
                results_of_rest = self.dfs(s[len(word):], word_dict)
                for item in results_of_rest:
                    item = f"{word} {item}"
                    result.append(item)
        self.memo[s] = result
        return result


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not self.is_breakable(s, wordDict): return []
        n, word_dict = len(s), set(wordDict)
        dp = [['']] + [[]] * n

        for i in range(1, n + 1):
            new_list = []
            for j in range(i):
                if not dp[j] or s[j:i] not in word_dict: continue
                new_list.extend([l + ('' if not l else ' ') + s[j:i] for l in dp[j]])
            dp[i] = new_list

        return dp[n]

    def is_breakable(self, s, word_dict):
        word_dict, n = set(word_dict), len(s)
        dp = [True] + [False] * n

        for i in range(1, n + 1):
            for j in range(i):
                if not dp[j] or s[j:i] not in word_dict: continue
                dp[i] = True
                break

        return dp[n]


# 140. Word Break II
# https://leetcode.com/problems/word-break-ii/description/



# Approach 1: DFS with Caching
# This approach is not ideal for interviews because,
# sometimes the interviewer says that the dictionary is not iterable
# and only gives you a API for checking containment

# Steps:
# 1. We iterate through dictionary and and for each word that the input string startswith()
#    we do a DFS to get results of the rest
# 2. We use the results of the rest from the next level of DFS and combine
#    the word with each of those results and return to the prev level

# Complexity Analysis
# Time:
# - Firstly n^2 to get every prefixes
# - Every prefix lets you branch for solving a smaller subproblem of size n - i (i.e n - 1, n - 2, n - 3, ... 1).
# So writing the recurrence for this would be:
# T(n) = n * (1 + T(n - 1) ) + (1 + T(n - 2) ) + ...... T(1)).
#   Here adding the "1" for each subproblem because the entire string is a solution itself,
#   and the factor of n for looping through the possible prefixes.
# PROOF: https://stackoverflow.com/questions/46004100/solving-this-recurrence-without-the-master-theorem-backtracking-algorithm
# This sums up to roughly n * 2^(n-1) which is O(n * 2^n) (Time and memory).
# Space:
# it's same for space as those 2^n can be a valid break, so the space complexity is also O(2^n)

# Time: O(n * 2^n)
# Space: O(n * 2^n)

# Approach 2: DP
# Firstly, check if the word is breakable, and only then do the actual breaking.
# Q: Why does this not take a long time?
# A: Cuz is_breakable() has earrly break for when a possible break is found.

# is_breakable() uses the DP below:
# dp[i] represents the bool of breakability of s[0:i] into words in wordDict
# for every j from 0 to i - 1
#   - dp[i] = True if dp[j] = True and s[j:i] is in the dict
#   - dp[0] = True, empty string is in the dict

# wordBreak() uses the DP below:
# dp[i] represents the actual words you can break s[0:i] from words in wordDict
# for every j from 0 to i - 1:
#   - If dp[j] is not empty and if s[j:i] is in the word_dict, we've found a break point so,
#   - Use the results of s[0:j] and combine those with s[0:j]
#   - Save list of these results as dp[i]

# Time: O(n^3)
# Space: O(n^3)

sol = Solution1()
wordDict = ["cat", "cats", "and", "sand", "dog"]
assert sorted(sol.wordBreak("catsanddog", wordDict)) == sorted([
    "cats and dog",
    "cat sand dog"
])
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
assert sorted(sol.wordBreak("pineapplepenapple", wordDict)) == sorted([
    "pine apple pen apple",
    "pineapple pen apple",
    "pine applepen apple"
])
wordDict = ["cats", "dog", "sand", "and", "cat"]
assert sol.wordBreak("catsandog", wordDict) == []
wordDict = [
    "a", "aa", "aaa",
    "aaaa", "aaaaa", "aaaaaa", "aaaaaaa",
    "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"
]
assert sol.wordBreak(
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    wordDict
) == []


sol = Solution()
wordDict = ["cat", "cats", "and", "sand", "dog"]
assert sorted(sol.wordBreak('catsanddog', wordDict)) == sorted([
    "cats and dog",
    "cat sand dog"
])
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
assert sorted(sol.wordBreak('pineapplepenapple', wordDict)) == sorted([
    "pine apple pen apple",
    "pineapple pen apple",
    "pine applepen apple"
])
wordDict = ["cats", "dog", "sand", "and", "cat"]
assert sol.wordBreak('catsandog', wordDict) == []
wordDict = [
    "a", "aa", "aaa",
    "aaaa", "aaaaa", "aaaaaa", "aaaaaaa",
    "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"
]
assert sol.wordBreak(
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    wordDict
) == []
