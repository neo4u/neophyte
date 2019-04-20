class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])


class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]

# 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/

# Time: O(n)
# Space: O(1)

# require 'test/unit'
# extend Test::Unit::Assertions

# assert_equal(reverse_string("reverse"), "esrever")
# assert_equal(reverse_string("abcd"), "dcba")
# assert_equal(reverse_string("cdc"), "cdc")
