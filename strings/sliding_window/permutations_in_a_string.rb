def check_inclusion(p, s)
    return false if s.size < p.size
    m, n = s.size, p.size
    curr, desired = [0] * 26, [0] * 26
    count = 0
    
    0.upto(p.size - 1) do |i|
        curr[s[i].ord - 'a'.ord] += 1
        desired[p[i].ord - 'a'.ord] += 1
    end
    0.upto(25) do |i|
        count += 1 if curr[i] == desired[i]
    end
    return true if count == 26

    1.upto(m - n) do |i|
        l = s[i - 1].ord - 'a'.ord
        r = s[i - 1 + n].ord - 'a'.ord
        count -= 1 if curr[l] == desired[l]
        curr[l] -= 1
        count += 1 if curr[l] == desired[l]

        count -= 1 if curr[r] == desired[r]
        curr[r] += 1
        count += 1 if curr[r] == desired[r]
        
        return true if count == 26
    end

    false
end


# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/
