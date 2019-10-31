class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        result = []
        for word in wordDict:
            if not s.startswith(word): continue

            if len(word) == len(s):
                result.append(word)
            else:
                results_of_rest = self.dfs(s[len(word):], wordDict, memo)
                for item in results_of_rest:
                    item = word + ' ' + item
                    result.append(item)

        memo[s] = result
        return result

# cat, cats, sand, and, dog

# catsanddog
