# @param {Character[]} chars
# @return {Integer}
def compress(chars)
    len = chars.size
    run_idx, out_idx = 0, 0

    chars.each do |c|
        while run_idx < len # Each time we enter this loop we've encountered a new char
            # Capture the current character (number) and reset count
            curr, count = chars[run_idx], 0

            # Keep looping forward until we encounter a new char and break from this small while loop
            while run_idx < len && chars[run_idx] == curr
                count += 1
                run_idx += 1
            end

            # Save the current char following by the count of the char. Count is saved char by char
            chars[out_idx], out_idx = curr, out_idx + 1

            next if count <= 1
            count.to_s.each_char do |i|
                chars[out_idx] = i
                out_idx += 1
            end
        end
    end
    chars = chars[0, out_idx]

    chars.size
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
