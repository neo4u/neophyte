class Solution:
    def find_strobogrammatic(self, n):
        strobo_odd_seed = ['0', '1', '8']
        strobo_even_seed = ['11', '69', '88', '96', '00']

        if n == 1: return strobo_odd_seed
        elif n == 2: return strobo_even_seed[:-1]
        elif n%2 == 1: outer, inner = self.find_strobogrammatic(n - 1), strobo_odd_seed
        elif n%2 == 0: outer, inner = self.find_strobogrammatic(n - 2), strobo_even_seed

        outer_mid, result = len(outer[0]) // 2, []
        for o in outer:
            for i in inner:
                l, r = o[:outer_mid], o[outer_mid:]
                result.append(l + i + r)

        return result


# 246. Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/

# Approach 1:

# NOTE: 00 is not part of n = 2 result because it's not even a number.
#       (Or rather, not the decimal representation of a number.)

# Insert from 1 or 2 solution middle of (n - 1)th or (n - 2)th solution respectively
# n == 1: [0, 1, 8]
# n == 2: [11, 88, 69, 96]
# How about n == 3
# => it can be retrieved if you insert each one of [0, 1, 8] in the middle of solution of n == 2
# n == 4?
# => it can be retrieved if you insert each one of [11, 88, 69, 96, 00] in the middle of solution of n == 2
# n == 5?
# => it can be retrieved if you insert each one of [0, 1, 8] to the middle of solution of n == 4
# the same, for n == 6, it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 4

sol = Solution()

assert sol.find_strobogrammatic(1) == ["0", "1", "8"]
assert sol.find_strobogrammatic(2) == ["11", "69", "88", "96"]
assert sol.find_strobogrammatic(3) == ["101", "111", "181", "609", "619", "689", "808", "818", "888", "906", "916", "986"]
assert sol.find_strobogrammatic(4) == [
    "1111", "1691", "1881", "1961", "1001", "6119", "6699",
    "6889", "6969",  "6009", "8118", "8698", "8888", "8968",
    "8008", "9116", "9696", "9886", "9966", "9006"
]
