# @param {String} s
# @param {String[]} word_dict
# @return {String[]}
def word_break(s, word_dict)
    bt(s, word_dict, {})
end

def bt(s, word_dict, map)
    return map[s] if map.key?(s)
    map[s] = [] if !map[s] # This is the init for a new key

    word_dict.each do |w|
        map[s] << s if w == s # This only happens at the deepest dfs level when we hit an actual word from the dictionary
        next if !s.start_with?(w)
        result_of_rest = bt(s[w.size...s.size], word_dict, map)
        result_of_rest.each do |other_w|
            map[s] << "#{w} #{other_w}"
        end
    end

    map[s]
end

# @param {String} s
# @param {String[]} word_dict
# @return {String[]}
def word_break_dp(s, word_dict)
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

# Approach 1: Brute-Force,                                  Time: O(n ^ n), Space: O(n ^ 3)

# Approach 2: Backtracking / Recursion with memoization,    Time: O(n ^ 3), Space: O(n ^ 3)
# Example: s = "catsanddog" word_dict = ["cat","cats","and","sand","dog"]
# bt call with catsanddog {}
# bt call with sanddog {"catsanddog"=>[]}
#     bt call with dog {"catsanddog"=>[], "sanddog"=>[]}
#         bt call with "" {"catsanddog"=>[], "sanddog"=>[], "dog"=>["dog"]}
#         bt return with "" {"catsanddog"=>[], "sanddog"=>[], "dog"=>["dog"], ""=>[]}
#     bt return with dog {"catsanddog"=>[], "sanddog"=>[], "dog"=>["dog"], ""=>[]}
# bt return with sanddog {"catsanddog"=>[], "sanddog"=>["sand dog"], "dog"=>["dog"], ""=>[]}
# bt call with anddog {"catsanddog"=>["cat sand dog"], "sanddog"=>["sand dog"], "dog"=>["dog"], ""=>[]}
#     bt call with dog {"catsanddog"=>["cat sand dog"], "sanddog"=>["sand dog"], "dog"=>["dog"], ""=>[], "anddog"=>[]}
# bt return with anddog {"catsanddog"=>["cat sand dog"], "sanddog"=>["sand dog"], "dog"=>["dog"], ""=>[], "anddog"=>["and dog"]}
# bt return with catsanddog {"catsanddog"=>["cat sand dog", "cats and dog"], "sanddog"=>["sand dog"], "dog"=>["dog"], ""=>[], "anddog"=>["and dog"]}

# bt call with catsanddog
# bt call with sanddog
#     bt call with dog
#         bt call with ""
#         bt return with ""
#     bt return with dog
# bt return with sanddog
# bt call with anddog
#     bt call with dog
# bt return with anddog
# bt return with catsanddog
# Find the recursion tree in the diagram attached.

# Approach 3: DP,                                           Time: O(n ^ 3), Space: O(n ^ 3)
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
#         and each activation record can contains a string list of size n.

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(word_break("catsanddog", ["cat","cats","and","sand","dog"]), ["cat sand dog", "cats and dog"])
assert_equal(word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), [])

assert_equal(word_break_dp("catsanddog", ["cat","cats","and","sand","dog"]), ["cat sand dog", "cats and dog"])
# TLE on below input
# assert_equal(word_break_dp("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), 0)
