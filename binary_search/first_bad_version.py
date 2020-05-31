
class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n

        while l < r:
            mid = (l + r) // 2

            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1

        return l


# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/description/
