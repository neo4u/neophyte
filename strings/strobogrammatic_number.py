class Solution:
    def is_strobogrammatic(self, num):
        if not num: return False
        strobo_set = set([
            ('0', '0'), ('8', '8'),
            ('9', '6'), ('6', '9'), ('1', '1')
        ])
        l, r = 0, len(num) - 1

        while l < r:
            if (num[l], num[r]) not in strobo_set: return False
            l += 1; r -= 1

        return True


# 246. Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/


# Time: O(n)
# Space: O(1)


sol = Solution()
assert sol.is_strobogrammatic("69")
assert sol.is_strobogrammatic("88")
assert sol.is_strobogrammatic("962")
