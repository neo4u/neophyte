# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
    shortest = strs.min_by(&:size)

    shortest.each_char.with_index do |c, i|
        strs.each do |str|
            return shortest[0, i] if str[i] != c
        end
    end
end

# 14. Longest Common Prefix

# Time: O(min(len(strs)))
# Space: O(1)

# Atleast 5 other approaches, check leetcode solutions
# Trie is another approach, but it needs more space. but time is lesser??? Not sure