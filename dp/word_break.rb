# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}

def word_break(s, word_dict)
  n = s.size
  dp, dp[0] = Array.new(n + 1, false), true
  1.upto(n) do |i|
    0.upto(i - 1) do |j|
      if dp[j] && word_dict.include?(s[j..(i - 1)])
        dp[i] = true
        break
      end
    end
  end
  dp[n]
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(word_break('asmartasssolution', ['a', 'smart', 'ass', 'solution']), true)
assert_equal(word_break('catsanddogs', ['cats', 'and', 'dogs']), true)
assert_equal(word_break('leetcode', ['leet', 'code']), true)

# the DP equation is:
# let "" be part of the dictionary and i be the start index and j be end index of string s[i...j]
# dp[i] is the bool representing if the substring of length i of the given string
# can be broken into dictionary words. Then...
#     dp[i] = d[j] && word_dict.include?(s[i...j])
# dp[n] is the boolean reprenting if the given string can be broken into dictionary words

# s = "silence"
# n = s.size
# counter = 0

# 1.upto(n) do |i|
#   0.upto(i - 1) do |j|
#     counter += 1
#     puts "#{counter}: #{s[j...i]}"
#   end
# end
