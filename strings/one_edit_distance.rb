def is_one_edit_distance(s, t)
    m, n = s.size, t.size
    s, t, m, n = t, s, n, m if m > n
    return false if s == t
    return false if n - m > 1

    0.upto(m - 1) do |i|
        next if s[i] == t[i]
        return s[i + 1...m] == t[i + 1...n] if m == n   # If equal len, check if mismatch char is replaceable
        return s[i...m] == t[i + 1...n]                 # If unqual len, check if mismatch char is deleteable
    end

    m + 1 == n                                          # If match upto m, then n must only have 1 extra deleteable char
end


# 161. One Edit Distance
# https://leetcode.com/problems/one-edit-distance/description/


