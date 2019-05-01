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


# def find_ladders_preprocess(begin_word, end_word, word_list)
#     return 0 if end_word.empty? || begin_word.empty? || word_list.empty?
#     paths, shortest = [], nil
#     n = begin_word.size
#     all_combo_dict = Hash.new { |h, k| h[k] = [] }
#     word_list.each do |word|
#         0.upto(n - 1) do |i|
#             generic_word = "#{word[0...i]}*#{word[i + 1...n]}"
#             all_combo_dict[generic_word] << word
#         end
#     end

#     q, visited = [[begin_word, [begin_word]]], Set.new([begin_word])
#     word_path[begin_word] = [[begin_word]]
#     while !q.empty?
#         curr_word, path = q.shift()
#         0.upto(n - 1) do |i|
#             next_word = "#{curr_word[0...i]}*#{curr_word[i + 1...n]}"
#             puts "curr_word: #{curr_word}, curr_path: #{path}, next_word: #{next_word}"
#             next if all_combo_dict[next_word].empty?

#             all_combo_dict[next_word].each do |word|
                
#                 next if visited.include?(word)
#                 visited.add(word)
#                 q.push([word, path + [word]])
#                 puts "q: #{q}"
#             end
#         end
#     end

#     paths
# end

# NOT WORKING
def find_ladders_preprocess(begin_word, end_word, word_list)
    return 0 if end_word.empty? || begin_word.empty? || word_list.empty?
    paths, shortest = [], nil
    level = 1
    n = begin_word.size
    all_combo_dict = Hash.new { |h, k| h[k] = [] }
    word_list.each do |word|
        0.upto(n - 1) do |i|
            generic_word = "#{word[0...i]}*#{word[i + 1...n]}"
            all_combo_dict[generic_word] << word
        end
    end

    p all_combo_dict
    q, visited = [[begin_word, [begin_word]]], Set.new([begin_word])
    while !q.empty?
        curr_word, path = q.shift()
        if path.size > level
            break if shortest && path.size > shortest
            level = path.size
            visited = Set.new()
            puts "clearing visite set for level: #{level}"
        end

        0.upto(n - 1) do |i|
            next_word = "#{curr_word[0...i]}*#{curr_word[i + 1...n]}"
            puts "curr_word: #{curr_word}, curr_path: #{path}, next_word: #{next_word}"
            next if all_combo_dict[next_word].empty?

            all_combo_dict[next_word].each do |word|
                puts "Trying #{word}"
                new_path = path + [word]
                next if shortest && new_path.size > shortest
                puts 'after next'
                if word == end_word
                    shortest = new_path.size if !shortest
                    paths.push(new_path)
                    next
                end
                next if visited.include?(word)
                visited.add(word)
                q.push([word, path + [word]])
                puts "q: #{q}"
            end
        end
    end

    paths
end

# https://leetcode.com/problems/word-ladder
# 127. Word Ladder

# To avoid TLE you must replace word_list with a Set.new(word_list)
# > Algo：BFS
# > Time Complexity O(n * 26 ^ l) where n = word_list.size and l = word.size
# > Space Complexity O(n) queue and visited


# {
#     "*ed"=>["ted", "red"],
#     "t*d"=>["ted", "tad"],
#     "te*"=>["ted", "tex"],
#     "*ex"=>["tex", "rex"],
#     "t*x"=>["tex", "tax"],
#     "r*d"=>["red"],
#     "re*"=>["red", "rex"],
#     "*ax"=>["tax"],
#     "ta*"=>["tax", "tad"],
#     "*ad"=>["tad"],
#     "*en"=>["den"],
#     "d*n"=>["den"],
#     "de*"=>["den"],
#     "r*x"=>["rex"],
#     "*ee"=>["pee"],
#     "p*e"=>["pee"],
#     "pe*"=>["pee"]
# }


require 'set'
require 'test/unit'
extend Test::Unit::Assertions

# assert_equal(find_ladders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]), [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]])


# assert_equal(find_ladders_preprocess('hit', 'cog', ["hot","dot","dog","lot","log","cog"]), [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]])

assert_equal(
    find_ladders_preprocess("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]),
    [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
)
