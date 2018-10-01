# @param {String} s
# @param {String[]} word_dict
# @return {String[]}
def word_break(s, word_dict)
    dfs(s, word_dict, {})
end

def dfs(s, word_dict, map)
    # puts "dfs call with #{s}"
    return map[s] if map.key?(s)
    map[s] = [] if !map[s] # This is the init for a new key

    word_dict.each do |w|
        map[s] << s if w == s # This only happens at the deepest dfs level when we hit an actual word from the dictionary
        next unless s.start_with?(w)
        # puts "Before deeper DFS, map is #{map[s]}"
        dfs(s[w.size...s.size], word_dict, map).each do |other_w|
            map[s] << "#{w} #{other_w}"
        end
        # puts "After deeper DFS, map is #{map[s]}"
    end
    map[s]
end

# 140. Word Break II
# https://leetcode.com/problems/word-break-ii/solution/

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(word_break("catsanddog", ["cat","cats","and","sand","dog"]), ["cat sand dog", "cats and dog"])
# Output for the above example.
# dfs call with catsanddog
# Before deeper DFS, map is []
# dfs call with sanddog
# Before deeper DFS, map is []
# dfs call with dog
# Before deeper DFS, map is ["dog"]
# dfs call with
# After deeper DFS, map is ["dog"]
# After deeper DFS, map is ["sand dog"]
# After deeper DFS, map is ["cat sand dog"]
# Before deeper DFS, map is ["cat sand dog"]
# dfs call with anddog
# Before deeper DFS, map is []
# dfs call with dog
# After deeper DFS, map is ["and dog"]
# After deeper DFS, map is ["cat sand dog", "cats and dog"]
assert_equal(word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), [])
# Output is useless for understanding for the above example.
