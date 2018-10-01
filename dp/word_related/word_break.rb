# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}
def word_break(s, word_dict)
    word_dict = Set.new(word_dict)  # makes the algorithm O(n^2) making the set containment checks O(1)
    n = s.size
    dp = Array.new(n + 1, false)
    dp[0] = true                    # We assume empty string to be part of dictionary and to be breakable

    1.upto(n) do |i|                # consider substrings of lengths from 1 to n
        0.upto(i - 1) do |j|                            # At every potential break point j that goes from 0 to i - 1 (length i) we check if:
            if dp[j] && word_dict.include?(s[j...i])    # 1. dp[j] == true (s[0...j] is breakable)
                dp[i] = true                            # 2. s[j...i] is in dictionary
                break               # break to next i because we found a breakpoint for the substrings of size i
            end
        end
    end

    dp[n]
end

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(word_break('asmartasssolution', ['a', 'smart', 'ass', 'solution']), true)
assert_equal(word_break('catsanddogs', ['cats', 'and', 'dogs']), true)
assert_equal(word_break('leetcode', ['leet', 'code']), true)

# the DP equation is:
# dp[i] represents if substring (0,i) is breakable.
# for each longer substring, we just need to check
# dp[n] is the boolean reprenting if the given string can be broken into dictionary words

# At every potential break point j that goes from 0 to i - 1 (length i) we check if:
# 1. dp[j] == true (s[0...j] is breakable)
# 2. s[j...i] is in dictionary
# if such a break point is found we're done
# Time: O(n)