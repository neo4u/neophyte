def is_one_edit_distance(s, t)
    m, n = s.size, t.size
    s, t, m, n = t, s, n, m if m > n # ensure len(s) > len(t)
    return false if s == t
    return false if n - m > 1

    0.upto(m - 1) do |i|
        next if s[i] == t[i]
        return s[i + 1...m] == t[i + 1...n] if m == n   # If equal len, check if mismatch char is replaceable
        return s[i...m] == t[i + 1...n]                 # If unqual len, check if mismatch char is deleteable
    end

    true
end


# 161. One Edit Distance
# https://leetcode.com/problems/one-edit-distance/description/
