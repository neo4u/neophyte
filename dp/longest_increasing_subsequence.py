from typing import List


# Approach 3: DP
class SolutionDP:
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


# Approach 4: Binary Search, Using bisect_left
import bisect
class SolutionBinSearch1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for n in nums:
            # Use bisect_left as we may have repeated numbers
            # In this case, do NOT want to insert at the end
            i = bisect.bisect_left(seq, n)
            if i == len(seq):
                seq.append(n)
            elif n < seq[i]: # we can use else: we don't just avoid an extra assignment for == case.
                seq[i] = n

        return len(seq)


# Approach 4: Binary Search, Custom Binary Search Implementation
class SolutionBinSearch2:
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


# Approach 4: Binary Search, Custom Binary Search Implementation with l <= r, instead of l < r, in binary search
class SolutionBinSearch3:
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


# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

# Approach 1: Brute-Force Time: O(2^n), Space: O(n^2)

# Approach 2: Recursion with memoization, Time: O(n^2), Space: O(n^2)

# Approach 3: DP, Time: O(n^2), Space: O(n)
# dp[i] represents length of LIS for nums[0:i]
# dp[i] = max(dp[j]) + 1 for j from 0 to i - 1 where nums[i] > nums[j]
# dp[0] = 1

# dp[n] is the answer

# Approach 4: Binary search, Time: O(nlog(n)), Space: O(1)


# RETURN the actual longest increasing sequence (LIS)
# Sort of expensive method, because of the copy() part
import bisect
class Solution4:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq, result = [], 0
        for n in nums:
            i = bisect.bisect_left(seq, n)
            if i == len(seq):
                seq.append(n)
                result = seq.copy() # Very expensive, much better solution below
            elif n < seq[i]:
                seq[i] = n

        print(result)
        return result


# Python version of:
# https://github.com/IDeserve/learn/blob/master/LongestIncreasingSubsequence.java
# https://www.youtube.com/watch?v=1RpMc3fv0y4&t=172s

class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> List[int]:
        n = len(nums)

        self.parent = [None] * n                    # Tracking the predecessors/parents of elements of each subsequence.
        self.inc_seq = [None] * (n + 1)             # Tracking ends of each increasing subsequence
        self.length = 0                             # Length of longest subsequence found so far

        for i in range(n):
            pos = self.bin_search_left(nums, nums[i])
            print(f"pos: {pos} | len: {self.length}")
            self.parent[i] = self.inc_seq[pos - 1]  # update parent/previous element for LIS
            self.inc_seq[pos] = i                   # Replace or append
            if pos > self.length: self.length = pos # Update the length of the longest subsequence.

        lis, k = [], self.inc_seq[self.length]
        while k is not None:              # Generate LIS by traversing parent array
            lis.append(nums[k])
            k = self.parent[k]

        return lis[::-1]

    def bin_search_left(self, a, x):
        l, r = 1, self.length

        while l <= r:
            mid = (l + r) // 2
            if a[self.inc_seq[mid]] < x:
                l = mid + 1
            else:
                r = mid - 1

        return l



# sol2 = Solution2()
# assert sol2.lengthOfLIS([-1, 0, 1, 10, 4, 5]) == [-1, 0, 1, 4, 5]
# assert sol2.lengthOfLIS([-1, 0, 1, 10, 20, 30, 4, 5]) == [-1, 0, 1, 10, 20, 30]
# assert sol2.lengthOfLIS([-1, 0, 1, 10, 20, 30, 4, 5, 6]) == [-1, 0, 1, 10, 20, 30]


sol3 = Solution3()
assert sol3.lengthOfLIS([-1, 0, 1, 10, 4, 5]) == [-1, 0, 1, 4, 5]
assert sol3.lengthOfLIS([-1, 0, 1, 10, 20, 30, 4, 5]) == [-1, 0, 1, 10, 20, 30]
assert sol3.lengthOfLIS([-1, 0, 1, 10, 20, 30, 4, 5, 6]) == [-1, 0, 1, 4, 5, 6]
assert sol3.lengthOfLIS([1, 3, 5, 4, 7]) == [1, 3, 4, 7]
assert sol3.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == [2, 3, 7, 18]
assert sol3.lengthOfLIS([3, 1, 5, 0, 6, 4, 9]) == [1, 5, 6, 9]
