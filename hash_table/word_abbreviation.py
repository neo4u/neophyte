from typing import List
import collections


# Approach 1: Greedy
class Solution1:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        n, result = len(words), list(map(self.get_abbr, words))
        prefix = [0] * n

        for i in range(n):
            while True:             # The while resolves dups and goes on until no dups are found
                dups = set()        # Compare abbr at i with every abbr after it
                for j in range(i + 1, n):
                    if result[i] != result[j]: continue
                    dups.add(j)

                if not dups: break
                dups.add(i)
                for k in dups:
                    prefix[k] += 1
                    result[k] = self.get_abbr(words[k], prefix[k])

        return result

    def get_abbr(self, word: str, i: int = 0):
        if len(word) - i <= 3: return word
        return word[:i + 1] + str(len(word) - i - 2) + word[-1]


# Approach 2: Group + Least Common Prefix
class Solution2:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        result = [None for _ in words]

        groups = collections.defaultdict(list)
        for i, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, i)) # len, start char, end char is the key, (word, index) is the value

        for dup_words in groups.values():
            print(f"dups: {dup_words}")
            dup_words.sort()
            print(f"dups: {dup_words}")
            lcp = [0] * len(dup_words)

            for i, (word, _) in enumerate(dup_words):
                print(f"Word: {word}")
                print(f"lcp Before: {lcp}")
                if i == 0: continue
                prev = dup_words[i - 1][0]
                lcp[i] = self.lcp_len(word, prev)
                lcp[i - 1] = max(lcp[i - 1], lcp[i])
                print(f"lcp After: {lcp}")

            for (word, index), p in zip(dup_words, lcp):
                result[index] = self.get_abbr(word, p)
            print(result)
            print()

        return result

    def lcp_len(self, a, b):
        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]: i += 1
        return i

    def get_abbr(self, word: str, i: int = 0):
        if len(word) - i <= 3: return word
        return word[:i + 1] + str(len(word) - i - 2) + word[-1]


# Approach 3: Groups + Trie
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        groups = collections.defaultdict(list)
        for i, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, i))

        result = [None] * len(words)
        Trie = lambda: collections.defaultdict(Trie)
        COUNT = False
        for group in groups.values():
            trie = Trie()
            for word, _ in group:
                cur = trie
                for letter in word[1:]:
                    cur[COUNT] = cur.get(COUNT, 0) + 1
                    cur = cur[letter]

            for word, index in group:
                cur = trie
                for i, letter in enumerate(word[1:], 1):
                    if cur[COUNT] == 1: break
                    cur = cur[letter]
                result[index] = self.get_abbr(word, i - 1)
        return result

    def get_abbr(self, word: str, i: int = 0):
        if len(word) - i <= 3: return word
        return word[:i + 1] + str(len(word) - i - 2) + word[-1]


# 527. Word Abbreviation
# https://leetcode.com/problems/word-abbreviation/description/

# Intuition:
# 1. We need to return the minimal set of unique abbreviations.
# 2. When two words collide on a standard abbreviation,
#    then we resolve collisions by adding chars to the abbr until no collision
# 3. We'll need a method to get_abbr given a word, optionally given an index,
#    which doesn't need to do anything for len <= 3 cuz the abbreviation is the same len in that case

# Approach 1: Greedy
# Steps:
# 1. We start off by having a result with all the words and their correspoding standard abbreviation
#    and then go resolving duplicates
# 2. To resolve dups we compare current abbr with every abbr index j after i which is a dup of abbr at index i
# 3. If we see that 'dups' is non-empty, then for every dup index k we +1 the prefix[k] in the prefix array
#    'prefix' array is used to track the prefix to be used for each 0 to n - 1

# Example 1:
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
# Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]

# word is: like
# No Dups
# word is: god
# No Dups

# word is: internal
# dups is: {2, 5}
# prefix[2]: 1
# abbr for internal is in5l
# prefix[5]: 1
# abbr for interval is in5l

# dups is: {2, 5}
# prefix[2]: 2
# abbr for internal is int4l
# prefix[5]: 2
# abbr for interval is int4l

# dups is: {2, 5}
# prefix[2]: 3
# abbr for internal is inte3l
# prefix[5]: 3
# abbr for interval is inte3l

# dups is: {2, 5}
# prefix[2]: 4
# abbr for internal is inter2l
# prefix[5]: 4
# abbr for interval is inter2l

# dups is: {2, 5}
# prefix[2]: 5
# abbr for internal is internal
# prefix[5]: 5
# abbr for interval is interval
# No More Dups

# word is: me
# No Dups
# word is: internet
# No Dups
# word is: interval

# word is: intension
# dups is: {8, 6}
# prefix[8]: 1
# abbr for intrusion is in6n
# prefix[6]: 1
# abbr for intension is in6n

# dups is: {8, 6}
# prefix[8]: 2
# abbr for intrusion is int5n
# prefix[6]: 2
# abbr for intension is int5n

# dups is: {8, 6}
# prefix[8]: 3
# abbr for intrusion is intr4n
# prefix[6]: 3
# abbr for intension is inte4n
# No More Dups

# word is: face
# No Dups
# word is: intrusion
# No Dups

# sol = Solution1()
# assert sol.wordsAbbreviation([
#     "like", "god", "internal",
#     "me", "internet", "interval",
#     "intension", "face", "intrusion"
# ]) == [
#     "l2e", "god", "internal",
#     "me", "i6t", "interval",
#     "inte4n", "f2e", "intr4n"
# ]

# Time: O(C^2)
# Space: O(C)

# Approach 2: Groups + Least Common Prefix
# Time: O(C * log(C))
# Space: O(C)

sol = Solution2()
assert sol.wordsAbbreviation([
    "like", "god", "internal",
    "me", "internet", "interval",
    "intension", "face", "intrusion"
]) == [
    "l2e", "god", "internal",
    "me", "i6t", "interval",
    "inte4n", "f2e", "intr4n"
]

# Approach 3: Groups + Trie
# Time: O(C)
# Space: O(C)

# sol = Solution()
# assert sol.wordsAbbreviation([
#     "like", "god", "internal",
#     "me", "internet", "interval",
#     "intension", "face", "intrusion"
# ]) == [
#     "l2e", "god", "internal",
#     "me", "i6t", "interval",
#     "inte4n", "f2e", "intr4n"
# ]