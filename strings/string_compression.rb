def compress(chars)
    n = chars.size
    w, r = 0, 0

    while r < n
        curr, count = chars[r], 0                                       # Read using read head 'r'
        r, count = r + 1, count + 1 while r < n && chars[r] == curr     # Read until diff char using 'r'

        chars[w], w = curr, w + 1                                       # Write the curr char using write head 'w'
        next if count <= 1                                              # if only 1 char, then we've already written it
        count.to_s.each_char { |i| chars[w], w = i, w + 1 }             # Write the count of char using write head 'w'
    end

    w
end

# Slight optimiation
def compress(chars)
    n = chars.size
    r, w = 0, 0

    while r < n
        curr, count = chars[r], 0
        count, r = count + 1, r + 1 while r < n && curr == chars[r]

        chars[w], w = curr, w + 1
        count.to_s.each_char { |i| chars[w], w = i, w + 1 } if count > 1
    end

    w
end


# 443. String Compression
# https://leetcode.com/problems/string-compression/description/


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(compress(["a","a","b","b","c","c","c"]), 6)
assert_equal(compress(["a"]), 1)
assert_equal(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]), 4)

