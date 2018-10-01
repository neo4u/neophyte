# @param {String} s
# @param {String[]} word_dict
# @return {String[]}
def word_break(s, word_dict)
    word_dict = Set.new(word_dict)
    n = s.size()
    dp = Array.new(n + 1)
    dp[0] = [""]

    1.upto(n) do |i|
        list = []
        0.upto(i - 1) do |j|
            if dp[j] && word_dict.include?(s[j...i])
                dp[j].each do |l|
                    list.push(l + (l.empty? ? "" : " ") + s[j...i])
                end
            end
        end
        dp[i] = list
    end

    dp[n]
end

# 140. Word Break II
# https://leetcode.com/problems/word-break-ii/solution/

# Leetcode DP solution 
# In the previous approach we can see that many subproblems were redundant,
# i.e we were calling the recursive function multiple times
# for the same substring appearing through multiple paths.
# To avoid this we can use memorization method,
# where we are making use of a hashmap to store the results in the form of a key:value pair.
# In this hashmap, the keykey used is the starting index of the string currently considered and
# the valuevalue contains all the sentences which can be formed
# using the substring from this starting index onwards.
# Thus, if we encounter the same starting index from different function calls,
# we can return the result directly from the hashmap rather than going for redundant function calls.

# With memorization many redundant subproblems are avoided and
# recursion tree is pruned and thus it reduces the time complexity by a large factor.

# Time:   O(n^3) => Size of recursion tree can go up to n^2. The creation of list takes n time.
# Space:  O(n^3) => The depth of the recursion tree can go up to n
#         and each activation record can contains a string list of size nn. 

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(word_break("catsanddog", ["cat","cats","and","sand","dog"]), ["cat sand dog", "cats and dog"])
# TLE on this input
# assert_equal(word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), 0)
