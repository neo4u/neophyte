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
