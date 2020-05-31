# @param {String} s
# @return {String[]}
def generate_palindromes(s)
    counts_map = Hash.new { |h, k| h[k] = 0 }
    odd_count, mid, result = 0, '', []
    s.each_char { |c| counts_map[c] += 1 }

    counts_map.each do |k, v|
        if v % 2 == 1
            odd_count += 1
            mid = k
        end
    end
    return [] if odd_count > 1

    to_permuate = ""
    counts_map.each { |k, v| to_permuate += k * (v / 2) }
    return [mid] if to_permuate.empty?()
    uniq_perms = permute_unique(to_permuate)

    uniq_perms.each do |perm|
        result.push(perm + mid + perm.reverse())
    end

    result
end


def permute_unique(s)
    s = s.chars
    @result = []
    bt(s, s.size, 0)
    @result
end

def bt(s, n, first)
    @result.push(s.dup.join()) if first == n - 1
    used = Set.new()

    first.upto(n - 1) do |i|
        next if used.include?(s[i])
        used.add(s[i])
        swap(s, first, i) if first != i
        bt(s, n, first + 1)
        swap(s, first, i) if first != i
    end
end

def swap(s, i, j)
    s[i], s[j] = s[j], s[i]
end


require 'set'

# 267. Palindrome Permutation II
# https://leetcode.com/problems/palindrome-permutation-ii/description/


# https://leetcode.com/problems/palindrome-permutation-ii/discuss/69717/Backtrack-Summary:-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)