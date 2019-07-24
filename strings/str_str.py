class RollingHash:
    def __init__(self, s):
        self.checksum = 0
        self.base, self.prime = 256, 101
        self.max_power = len(s) - 1
        for c in s: self.add(c)

    def add(self, c):
        self.checksum = (self.checksum * self.base + ord(c)) % self.prime

    def remove(self, c):
        self.checksum = (self.checksum - (ord(c) * self.base**self.max_power)) % self.prime

    def __eq__(self, other):
        return self.checksum == other.checksum


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1
        m, n = len(haystack), len(needle)
        if n > m: return -1

        hh, hn = RollingHash(haystack[:n]), RollingHash(needle)
        if hh == hn and haystack[:n] == needle: return 0

        for i in range(1, m - n + 1):
            hh.remove(haystack[i - 1])
            hh.add(haystack[i - 1 + n])
            if hh == hn and haystack[i:i + n] == needle: return i

        return -1


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

sol = Solution()

assert sol.strStr('hello', 'll') == 2
assert sol.strStr('abbbbddddabcdsadf', 'abc') == 9
assert sol.strStr("hello there I am sam", "I am s") == 12
assert sol.strStr(
        "abaaabbabbaabaababaababbabababaababbbababbaababbabbbbaababaaaaabababbbaaaabbbaabaaababbaabaaabaaaaaaaaaaababaaaaabbbaabaaaaabaabbabbaabbbbababbaabbabbabbabababaabbbbaaaaaaabbabaababbbaab",
        "bbbbbaaabaaaabaaabbaabbaabbabaaabbbbabbbb"
) == -1

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
