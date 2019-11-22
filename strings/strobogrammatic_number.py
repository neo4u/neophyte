class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num: return False
        strobo_set = set([
            ('0', '0'), ('1', '1'),
            ('6', '9'), ('8', '8'), ('9', '6'),
        ])
        l, r = 0, len(num) - 1

        while l <= r:
            if (num[l], num[r]) not in strobo_set: return False
            l += 1; r -= 1

        return True


# 246. Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/


# Time: O(n)
# Space: O(1)


sol = Solution()
assert sol.isStrobogrammatic("69")
assert sol.isStrobogrammatic("88")
assert sol.isStrobogrammatic("962")
