# @param {String} s
# @param {String[]} word_dict
# @return {String[]}
def word_break(s, word_dict)
    dfs(s, word_dict, {})
end

def dfs(s, word_dict, map)
    return map[s] if map.key?(s)
    map[s] = [] if !map[s] # This is the init for a new key

    word_dict.each do |w|
        map[s] << s if w == s # This only happens at the dfs depth when we hit an actual word from the dictionary
        next unless s.start_with?(w)
        dfs(s[w.size...s.size], word_dict, map).each do |other_w|
            map[s] << "#{w} #{other_w}"
        end
    end
    map[s]
end

# 140. Word Break II
# https://leetcode.com/problems/word-break-ii/solution/

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(word_break("catsanddog", ["cat","cats","and","sand","dog"]), ["cat sand dog", "cats and dog"])
# Call output
# dfs() with word: catsanddog
# dfs() with word: sanddog
# dfs() with word: dog
# dfs() with word:
# returning []
# returning ["dog"]
# returning ["sand dog"]
# dfs() with word: anddog
# dfs() with word: dog
# returning ["and dog"]
# returning ["cat sand dog", "cats and dog"]
assert_equal(word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), [])
# Output is useless for understanding.
