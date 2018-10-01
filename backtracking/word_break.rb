# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}
def word_break(s, word_dict)
    dfs(s, Set.new(word_dict), Set.new())    # use of set for faster access time to make dfs
end

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

# 139. Word Break
# https://leetcode.com/problems/word-break/

# Time: O(n^2)
# Space: O(n)

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(word_break('asmartasssolution', ['a', 'smart', 'ass', 'solution']), true)
assert_equal(word_break('catsanddogs', ['cats', 'and', 'dogs']), true)
assert_equal(word_break('leetcode', ['leet', 'code']), true)
