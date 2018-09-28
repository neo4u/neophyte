# @param {String} begin_word
# @param {String} end_word
# @param {String[]} word_list
# @return {Integer}
def find_ladders(begin_word, end_word, word_list)
    n = begin_word.size
    q, word_list, visited, word_path = [begin_word], Set.new(word_list), Set.new([begin_word]), Hash.new([])
    word_path[begin_word] = [[begin_word]]

    while !q.empty?
        word = q.shift
        visited.add(word)

        0.upto(n - 1) do |i|
            l, r = word[0...i], word[i + 1...n]
            'a'.upto('z') do |c|
                next if word[i] == c
                next_word = l + c + r
                next if !word_list.include?(next_word) || visited.include?(next_word)

                q.push(next_word) if !q.include?(next_word) # The condition is to avoid adding same unvisited word to q

                word_path[word].map { |path_parent| path_parent + [next_word] }.each do |path|
                    break if !word_path[next_word].empty? && word_path[next_word][-1].length != path.length
                    word_path[next_word] += [path.dup]
                end
            end
        end
    end

    word_path[end_word]
end

# https://leetcode.com/problems/word-ladder
# 127. Word Ladder

# To avoid TLE you must replace word_list with a Set.new(word_list)
# > Algo：BFS
# > Time Complexity O(n * 26 ^ l) where n = word_list.size and l = word.size
# > Space Complexity O(n) queue and visited

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_ladders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]), [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]])
