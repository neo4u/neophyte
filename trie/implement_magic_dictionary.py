import collections
from typing import List
import pprint


# Approach 1: Hash Table
class MagicDictionary2:
    def _candidates(self, word):
        n = len(word)
        for i in range(n):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        self.words = set(words)
        self.near = collections.Counter(cand for word in words
                                        for cand in self._candidates(word))
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.near)

    def search(self, word):
        for cand in self._candidates(word):
            print(f"cand: {cand}")
            if self.near[cand] > 1 \
                or self.near[cand] == 1 \
                and word not in self.words:
                return True
        return False


from collections import defaultdict


# class MagicDictionary1:

#     def __init__(self):
#         pass

#     def buildDict(self, dict):
#         # key - the fuzzy word with star
#         # value - occurrence

#         self.lookup = defaultdict(int)
#         self.words = set(dict)

#         for word in self.words:
#             for i in self.get_fuzzy(word):
#                 self.lookup[i] += 1

#     def search(self, word: str) -> bool:
#         """Returns if there is any word in the trie that equals to the given word after modifying exactly one character"""
#         for i in self.get_fuzzy(word):
#             if self.lookup[i] >= 2 or (self.lookup[i] == 1 and word not in self.words):
#                 return True
#         return False

#     def get_fuzzy(self, word):
#         for i in range(len(word)):
#             yield word[:i] + '*' + word[i + 1:]




# Approach 2: Trie
# time O(len(word) * len(dictionary),
# space O(num of unique prefix) for trie
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

TAB = '\t'

class MagicDictionary:
    def __init__(self):
        self.trie = TrieNode()

    def _add(self, w):
        node = self.trie
        for c in w: node = node.children[c]
        node.is_word = True

    def _dfs(self, node: 'Node', word: str, depth=0) -> bool:
        print(f'{TAB * depth}dfs call with word: {word}')
        for c in word:
            if c not in node.children: return False
            node = node.children[c]

        print(f'{TAB * depth}is_word: {node.is_word}')
        return node.is_word

    def buildDict(self, words: List[str]) -> None:
        for w in words: self._add(w)

    def search(self, word: str) -> bool:
        node = self.trie
        for i, c in enumerate(word):
            print(f'c: {c}')
            for child_c in node.children:
                print(f'child_c: {child_c}')

                if c == child_c:
                    print('continuing')
                    continue
                dfs_ret = self._dfs(node.children[child_c], word[i + 1:])
                print(f'dfs ret: {dfs_ret}')
                if dfs_ret: return True

            if c not in node.children:
                print(f'c not in children')
                return False
            print('going deeper node')
            node = node.children[c]

        return False


# 676. Implement Magic Dictionary
# https://leetcode.com/problems/implement-magic-dictionary/description/


# Intuition:
# Similar to: https://leetcode.com/discuss/interview-question/643158/google-phone-faulty-keyboard


# Approach 1: Hash Table

# - A word 'apple' has neighbors '*pple', 'a*ple', 'ap*le', 'app*e', 'appl*'.
# - When searching for a target word like 'apply',
#   we know that a necessary condition is a neighbor of 'apply'
#   is a neighbor of some source word in our magic dictionary.
# - If there is more than one source word that does this,
#   then at least one of those source words will be different from the target word.
#   Otherwise, we need to check that the source doesn't equal the target.


# section complexity
# K - length of search word
# w - average length of each_word in dic
# If counting the time for constructing string
# Time - O(K^2) for search since we create new string every time, which technically takes time K
# Space - O(Sum(w^2))

# If not counting the time for constructing string
# Time - O(K) for search
# Space - for build Sum(w)


# Approach 2: Trie
# Time: O(len(word) * len(dictionary),
# Space: O(num of unique prefix) for trie

dic = MagicDictionary()
dic.buildDict(["hello", "leetcode"])
# assert dic.search("hello") is False
# assert dic.search("hhllo") is True
assert dic.search("jello") is True

# assert dic.search("helld") is True
# assert dic.search("hell") is False
# assert dic.search("leetcoded") is False
# assert dic.search("leetcode") is False
# assert dic.search("leepcode") is True

# assert dic.search("leotcode") is True
# assert dic.search("oeotcode") is False

# assert dic.search("hello") is False




# dic = MagicDictionary2()
# dic.buildDict(["hello", "hallo", "leetcode"])
# # assert dic.search("hhllo") is True
# assert dic.search("hello") is True
# assert dic.search("helld") is True
# assert dic.search("hell") is False
# assert dic.search("leetcoded") is False

# assert dic.search("helld") is True
# assert dic.search("hell") is False
# assert dic.search("leetcoded") is False
# assert dic.search("leotcode") is True
# assert dic.search("oeotcode") is False
# assert dic.search("hello") is False
