class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


import bisect
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for n in nums:
            # Use bisect_left as we may have repeated numbers
            # In this case, do NOT want to insert at the end
            i = self.bisect_left(seq, n)
            if i == len(seq):
                seq.append(n)
            elif n < seq[i]: # we can use else: we don't just avoid an extra assignment for == case.
                seq[i] = n

        return len(seq)

class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for n in nums:
            # Use bisect_left as we may have repeated numbers
            # In this case, do NOT want to insert at the end
            i = self.binary_search_left(seq, n)
            if i == len(seq):
                seq.append(n)
            elif n < seq[i]:
                seq[i] = n

        return len(seq)

    def binary_search_left(self, a, x):
        l, r = 0, len(a)

        while l < r:
            mid = (l + r) // 2

            if a[mid] < x:
                l = mid + 1
            else:
                r = mid

        return l

# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

# Approach 1: Brute-Force Time: O(2^n), Space: O(n^2)
# Approach 2: Recursion with memoization, Time: O(n^2), Space: O(n^2)
# Approach 3: DP, Time: O(n^2), Space: O(n)
# Approach 4: DP with binary search, Time: O(nlog(n)), Space: O(1)


# 1 1 1 1 1 2 5
#         l r
# 3

# l 0 r 2
# mid 1
# a[1] 2 < 3
# l 2 r 2


# [10, 9, 2, 5, 3, 7, 101, 18]

# i = 2
# j =  0, 1

# [0 1 1 1 1 1 1 1 1]

# dp[i] represents length of LIS for nums[0:i]
# dp[i] = max(dp[j]) + 1 for j from 0 to i - 1 where nums[i] > nums[j]
# dp[0] = 1

# dp[n] is the answer



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for n in nums:
            # Use bisect_left as we may have repeated numbers
            # In this case, do NOT want to insert at the end
            i = self.binary_search_left(seq, n)
            if i == len(seq):
                seq.append(n)
            elif n < seq[i]:
                seq[i] = n

        return len(seq)

    def binary_search_left(self, a, x):
        l, r = 0, len(a) - 1

        while l <= r:
            mid = (l + r) // 2
            if a[mid] == x: return mid
            if a[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

        return l