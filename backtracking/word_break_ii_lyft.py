# def wordBreak(self, s, wordDict):
#     res = []
#     self.dfs(s, wordDict, '', res)
#     return res

# def dfs(self, s, dic, path, res):
# # Before we do dfs, we check whether the remaining string 
# # can be splitted by using the dictionary,
# # in this way we can decrease unnecessary computation greatly.
#     if self.check(s, dic): # prunning
#         if not s:
#             res.append(path[:-1])
#             return # backtracking
#         for i in xrange(1, len(s)+1):
#             if s[:i] in dic:
#                 # dic.remove(s[:i])
#                 self.dfs(s[i:], dic, path+s[:i]+" ", res)

# # DP code to check whether a string can be splitted by using the 
# # dic, this is the same as word break I.                
# def check(self, s, dic):
#     dp = [False for i in xrange(len(s)+1)]
#     dp[0] = True
#     for i in xrange(1, len(s)+1):
#         for j in xrange(i):
#             if dp[j] and s[j:i] in dic:
#                 dp[i] = True
#     return dp[-1]



# write a function to deconstruct a string input, return the deconstructed string as a list of strings. If the input string is not entirely tokenizable, return an empty list.
# input: thequickbrownfox, dictionary=['t', 'th', 'the', 'theq', 'qui', 'quic', 'quick', 'brow', 'brown', 'fox']
# output: ['the', 'quick', 'brown', 'fox']

# thequickbrownfox


#class Dictionary():
#    def get(self, word):
#        return True/False    
from typing import List


    
class WordBreak():
    def word_break(self, s: str, word_dict: List[str]):
        return self.recurse(s, word_dict)

    def recurse(self, s: str, word_dict: List[str]):
        print(f"recurse call with: {s}")
        if s in word_dict: return [s]

        for i in range(len(s) + 1):
            if s[:i + 1] not in word_dict:
                print(f"{s[:i + 1]} not in word_dict")
                continue
            result_of_rest = self.recurse(s[i + 1:], word_dict)
            if result_of_rest:
                result = [s[:i + 1]] + result_of_rest
                print(f"result is {result}")
                return result
        return []

sol = WordBreak()
assert sol.word_break('thequickbrownfox', ['t', 'th', 'the', 'theq', 'qui', 'quic', 'quick', 'brow', 'brown', 'fox']) == ['the', 'quick', 'brown', 'fox']