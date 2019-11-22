from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}

        for i, num in enumerate(nums):
            if num in num_map and abs(i - num_map[num]) <= k: return True
            num_map[num] = i

        return False


# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii


sol = Solution()
assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1), True
assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3), True
assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2), False
