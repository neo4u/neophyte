# Approach 1: Hash pattern/word as key and word/pattern as value
# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern(pattern, str)
    words = str.split()
    return false if pattern.size != words.size

    p_hash, w_hash = {}, {}
    0.upto(words.size - 1) do |i|
        p, w = pattern[i], words[i]
        if (p_hash.key?(p) && p_hash[p] != w) || (w_hash.key?(w) && w_hash[w] != p)
            return false
        end

        p_hash[p], w_hash[w] = w, p
    end

    true
end

# Approach 2: Hash map with key as pattern/word with values as indexes
# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern(pattern, str)
    words = str.split()
    return false if pattern.size != words.size
    
    p_hash, w_hash = {}, {}
    0.upto(words.size - 1) do |i|
        p, w = pattern[i], words[i]
        if p_hash.key?(p)
            return false if !w_hash.key?(w) || w_hash[w] != p_hash[p]
        else
            p_hash[p] = i
        end

        if w_hash.key?(w)
            return false if !p_hash.key?(p) || w_hash[w] != p_hash[p]
        else
            w_hash[w] = i
        end
    end
    
    true
end