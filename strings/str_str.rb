class RollingHash
    include Comparable
    attr :checksum
    BASE = 256
    PRIME = 101

    def initialize(s)
        @max_power = s.size - 1 # This will be used as the power of base for removal or outgoing char from window
        @checksum = 0
        s.each_char { |c| add(c) }
    end

    # Think left bit shift, Increase power of all digits by base power 1 and add char * base power 0 => (checksum * BASE + c.ord)
    def add(c)
        @checksum = (@checksum * BASE + c.ord) % PRIME
    end

    # Think removing the MSB, so minus (c.ord * BASE**SIZE - 1) from checksum, 
    def remove(c)
        @checksum = (@checksum - (c.ord * BASE**@max_power)) % PRIME
    end

    def <=>(other_object)
        @checksum <=> other_object.checksum
    end
end

# Approach 3: Rolling Hash (Optimal)
# @param {String} haystack
# @param {String} needle
# @return {Integer}
def str_str(haystack, needle)
    return 0 if !needle || needle.empty?
    return -1 if !haystack || haystack.empty?
    m, n = haystack.size, needle.size
    return -1 if n > m

    hh, hn = RollingHash.new(haystack[0...n]), RollingHash.new(needle)
    return 0 if hh == hn && haystack[0...n] == needle

    1.upto(m - n) do |i|
        hh.remove(haystack[i - 1])
        hh.add(haystack[i - 1 + n])
        return i if hh == hn && haystack[i...i + n] == needle
    end

    -1
end


# Approach 1: O(m * n)
def str_str(haystack, needle)
    m, n = haystack.size, needle.size
    return 0 if !needle || needle.empty?
    return -1 if !haystack || haystack.empty? || n > m

    0.upto(m - n) do |i|
        0.upto(n - 1) do |j|
            break if haystack[i + j] != needle[j]
            return i if j == n - 1
        end
    end

    -1
end

# abcdef
# i   |
# ef


# Approach 1: Search from each index for pattern.length chars
# Time: O(m * n)
# Space: O(1)

# Approach 2: Keep a hash map of counts from needle and a map of counts for curr window into string
# Time: O(m + n)
# Space: O(26) or O(1)

# Approach 3: Rolling Hash
# Rolling Hash using Rabin Karp Algorithm
# http://pit-claudel.fr/clement/blog/linear-time-probabilistic-pattern-matching-and-the-rabin-karp-algorithm/
# Sudo Code/ Steps
# matches = {}
# p
# pattern_checksum = checksum(pattern)              # pattern of size n
# substring_checksum = checksum(s[0 to n-1])        # string of size m, substring of size n - 1
# for i from 0 to m - n do
#   update substring_checksum to checksum(s[i to i + n)
#   if substring_checksum = pattern_checksum thena
#     add position to matches
# return matches

# Key Insight
# 1. Think of the hashing of the string as converting a string to its decimal equivalent
#    Where, 256 is the base of the decimal conversion, like 2 is the base in converting binary to decimal
# 2. 

# Steps:
# 1. Keep a rolling hash for the pattern and the string
# 2. Initially just calculate the hash for the needle and the first n chars of haystack.
#    If the hashes match then return 0, also 
# 3. Iterate through all indices on the string and recompute hash for that window of size n (needle size)

# Time: O(m + n)
# Space: O(1)


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(str_str('hello', 'll'), 2)
assert_equal(str_str('abbbbddddabcdsadf', 'abc'), 9)
assert_equal(str_str("hello there I am sam", "I am s"), 12)
assert_equal(
    str_str(
        "abaaabbabbaabaababaababbabababaababbbababbaababbabbbbaababaaaaabababbbaaaabbbaabaaababbaabaaabaaaaaaaaaaababaaaaabbbaabaaaaabaabbabbaabbbbababbaabbabbabbabababaabbbbaaaaaaabbabaababbbaab",
        "bbbbbaaabaaaabaaabbaabbaabbabaaabbbbabbbb"
    ),
    -1
)

# assert_equal(str_str_rh('hello', 'll'), 2)
# assert_equal(str_str_rh('abbbbddddabcdsadf', 'abc'), 9)
# assert_equal(str_str_rh("hello there I am sam", "I am s"), 12)
# 100.times {
#     assert_equal(
#         str_str_rh(
#             "abaaabbabbaabaababaababbabababaababbbababbaababbabbbbaababaaaaabababbbaaaabbbaabaaababbaabaaabaaaaaaaaaaababaaaaabbbaabaaaaabaabbabbaabbbbababbaabbabbabbabababaabbbbaaaaaaabbabaababbbaab",
#             "bbbbbaaabaaaabaaabbaabbaabbabaaabbbbabbbb"
#         ),
#         -1
#     )
# }
