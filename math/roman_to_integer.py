class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_i = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        prev, val = 0, 0
        for c in reversed(s):
            curr = roman_to_i[c]
            val += curr if curr >= prev else -curr
            prev = curr

        return val


# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/


sol = Solution()
assert sol.roman_to_int('XVIII') == 18
assert sol.roman_to_int('xviii') == 18
assert sol.roman_to_int('I') == 1
assert sol.roman_to_int('MMD') == 2500
assert sol.roman_to_int('IX') == 9
assert sol.roman_to_int('X') == 10
assert sol.roman_to_int('IIIX') == 11
