from typing import List


# Approach 1: Sliding Window, Time: O(n * log(n)), Space: O(1)
class Solution1:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        window_sum, l, result = 0, 0, len(nums) + 1

        for r, num in enumerate(nums):  # Expand window to the right
            window_sum += num

            while window_sum >= s:      # Resize window from left
                result = min(result, r - l + 1)
                window_sum -= nums[l]
                l += 1

        return result if result <= len(nums) else 0


# Approach 2: Sliding Window + Binary Search, Time: O(n * log(n)), Space: O(n)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        result = len(nums) + 1
        for idx, num in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + num

        l = 0
        for r, n in enumerate(nums):
            if n >= s:
                l = self.find_left(l, r, nums, s, n)
                result = min(result, r - l + 1)

        return result if result <= len(nums) else 0

    def find_left(self, l, r, nums, s, num):
        while l < r:
            mid = (l + r) // 2

            if num - nums[mid] >= s:
                l = mid + 1
            else:
                r = mid

        return l


# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/


# Approach 1: Sliding Window
# Time: O(n)

# Approach 2: Sliding Window + Binary Search
# Time: O(nlog(n))
