# @param {String} s
# @param {String} p
# @return {Integer[]}
def find_anagrams(s, p)
    return [] if s.size < p.size
    
    m, n, result = s.size, p.size, []
    curr, desired = [0] * 26, [0] * 26
    
    0.upto(p.size - 1) do |i|
        curr[s[i].ord - 'a'.ord] += 1
        desired[p[i].ord - 'a'.ord] += 1
    end
    result.push(0) if curr == desired
    
    1.upto(m - n) do |i|
        curr[s[i - 1].ord - 'a'.ord] -= 1
        desired[s[i - 1 + n].ord - 'a'.ord] += 1
        result.push(i) if curr == desired
    end
    
    result
end

# @param {String} s
# @param {String} p
# @return {Integer[]}
def find_anagrams(s, p)
    return [] if s.size < p.size        # Can't have an anagram without all the chars from p

    m, n = s.size, p.size
    h1, h2 = [0] * 26, Array.new(26, 0) # Both are same, just for variety
    result = []

    # Take a snapshort of p's and s's count in h2 and h1 (for s its only upto length n)
    0.upto(p.size - 1) do |i|
        h2[s[i].ord - 'a'.ord] += 1
        h1[p[i].ord - 'a'.ord] += 1
    end

    result.push(0) if h1 == h2
    1.upto(m - n) do |i|
        h1[s[i - 1].ord - 'a'.ord] -= 1     # Remove from window
        h1[s[i - 1 + n].ord - 'a'.ord] += 1 # Add to window
        result.push(i) if h1 == h2          # If snapshot of window looks like snapshot of p, then add to result
    end

    result
end

# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string

# All the similar questions are:
# https://leetcode.com/problems/minimum-window-substring/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# https://leetcode.com/problems/find-all-anagrams-in-a-string/