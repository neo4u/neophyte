# @param {Integer} n, a positive integer
# @return {Integer}
def hamming_weight(n)
    # bits, mask = 0, 1
    bits = 0
    32.times do |i|
        mask = 2 ** i # you can also do mask <<= 1 after the next line of code starting from mask = 1
        bits += 1 if !(n & mask).zero?
    end

    bits
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(hamming_weight(0), 0) # "0"
assert_equal(hamming_weight(1), 1) # "1"
assert_equal(hamming_weight(3), 2) # "11"
assert_equal(hamming_weight(5), 2) # "101"

# public class Solution
# {
#     public int HammingDistance(int x, int y)
#     {
#         return NumberOf1Bits(x ^ y);
#     }

#     private int NumberOf1Bits(int n)
#     {
#         int count = 0;

#         while (n != 0)
#         {
#             count += n & 1;
#             n = n >> 1;
#         }

#         return count;
#     }
# }
