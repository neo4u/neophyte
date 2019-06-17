# DFS / Recursion with memoization
# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}
def word_break(s, word_dict)
    dfs(s, Set.new(word_dict), Set.new())    # use of set for faster access time to make dfs
end

# s = "catsandog"
# catsandog
#     sandog
#         og
#     andog
#         og

# wordDict = ["cat", "cats", "and", "sand", "dog"]

def dfs(s, word_dict, checked)
    return true if !s || s.empty?   # empty string is considered to be a match
    return false if checked.include?(s)

    checked.add(s)
    n = s.size()

    word_dict.each do |w|
        m = w.size()
        return true if s.start_with?(w) && dfs(s[m...n], word_dict, checked)
    end

    false
end

# Approach 3: BFS
def word_break_bfs(s, word_dict)
    return true if !s || s.empty?
    word_dict = Set.new(word_dict)
    q, visited, n = [0], Set.new(), s.size

    while !q.empty?
        i = q.shift()
        next if visited.include?(i)
        (i + 1).upto(n) do |j|
            next if !word_dict.include?(s[i...j])
            return true if j == s.size
            q.push(j)
        end
        visited.add(i)
    end

    false
end

# s = "catsandog"
# catsandog
# 0 q [2, 3] v:[0]
# 2 q [3] v:[0, 2]
# 3 q [6] v:[0, 2, 3]
# 6 q [8] v: [0, 2, 3, 6]
# 8 q []  v; [0, 2, 3, 6, 8]

# wordDict = ["cat", "cats", "and", "sand", "dog"]


# Approach 4: DP
def word_break_dp(s, word_dict)
    return true if !s || s.empty?
    word_dict, n = Set.new(word_dict), s.size           # makes the algorithm O(n^2) making the set containment checks O(1)
    dp = Array.new(n + 1, false)
    dp[0] = true                                        # We assume empty string to be part of dictionary and to be breakable

    1.upto(n) do |i|                                    # consider substrings of lengths from 1 to n
        0.upto(i - 1) do |j|                            # At every potential break point j that goes from 0 to i - 1 (length i) we check if:
            if dp[j] && word_dict.include?(s[j...i])    # 1. dp[j] == true (s[0...j] is breakable)
                dp[i] = true                            # 2. s[j...i] is in dictionary
                break                                   # break to next i because we found a breakpoint for the substrings of size i
            end
        end
    end

    dp[n]
end


# 139. Word Break
# https://leetcode.com/problems/word-break/

# Approach 1: Brute-Force,                  Time: O(n ^ n), Space: O(n)

# Approach 2: Recursion with memoization,   Time: O(n ^ 2), Space: O(n)

# Approach 3: BFS,                          Time: O(n ^ 2), Space: O(n)

# Approach 4: DP,                           Time: O(n ^ 2), Space: O(n)
# the DP equation is:
# dp[i] represents if substring s[0,i - 1] (length i) is breakable.
# dp[n] is the boolean reprenting if the given string can be broken into dictionary words

# At every potential break point j that goes from 0 to i - 1 (length i) we check if:
# 1. dp[j] == true (s[0...j] is breakable)
# 2. s[j...i] is in dictionary
# if such a break point is found we're done
# Time: O(n ^ 2), Space: O(n)

# Approach 5: Trie

# The whole problem resembles somehow NFA since problem gets more complex for the words with same prefix.
# E.g. s = "catsand" words = ["cat", "catsa", "sand", "nd"]. This way, when we are done with prefix "cat" we can either start from root or continue from the node where we finished, since it may be possible to transition from this node.

# Therefore if we think of the TrieNodes as states in NFA then all we need to do, is

# for every char (action in NFA)
# transition from one state to another (if possible)
# in order to simulate eps transition (if node has end_word property) we add root to the list of states to transition
# return true if any of the states are in accepting states set aka if any of the nodes has end_word property set to true

# class TrieNode:
#     def __init__(self):
#         self.transition = {}
#         self.end_word = False
    
#     def add_word(self, word):
#         if len(word) == 0: 
#             self.end_word = True
#             return
        
#         first, rest = word[0], word[1:]
        
#         next_node = TrieNode() if first not in self.transition else self.transition[first]
#         self.transition[first] = next_node
#         next_node.add_word(rest)

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def add_word(self, word):
#         self.root.add_word(list(word))

#     def traverse(self, s):
#         def transition(node, char):
#             return node.transition[char] if char in node.transition else None
#         states = [self.root]
#         for char in s:
#             new_states = []
#             append_root_only_once = True
#             for state in states:
#                 if state.end_word and append_root_only_once: 
#                     states.append(self.root)
#                     append_root_only_once = False
#                 new_state = transition(state, char)
#                 if new_state is not None: new_states.append(new_state)
#             states = new_states
#         return any([state.end_word for state in states])


# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         trie = Trie()
#         for word in wordDict: trie.add_word(word)
#         return trie.traverse(s)

# Best case
# Time: O(n^2)
# Space: O(n)

assert_equal(word_break('asmartasssolution', ['a', 'smart', 'ass', 'solution']), true)
assert_equal(word_break('catsanddogs', ['cats', 'and', 'dogs']), true)
assert_equal(word_break('leetcode', ['leet', 'code']), true)

assert_equal(word_break_bfs('asmartasssolution', ['a', 'smart', 'ass', 'solution']), true)
assert_equal(word_break_bfs('catsanddogs', ['cats', 'and', 'dogs']), true)
assert_equal(word_break_bfs('leetcode', ['leet', 'code']), true)

assert_equal(word_break_dp('asmartasssolution', ['a', 'smart', 'ass', 'solution']), true)
assert_equal(word_break_dp('catsanddogs', ['cats', 'and', 'dogs']), true)
assert_equal(word_break_dp('leetcode', ['leet', 'code']), true)
