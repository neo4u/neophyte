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

# ------------------------------------------------------------------------------------------------
# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.
# Follow up:
# Could you solve it using only O(1) extra space?
# ------------------------------------------------------------------------------------------------

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(compress(["a","a","b","b","c","c","c"]), 6)
assert_equal(compress(["a"]), 1)
assert_equal(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]), 4)

