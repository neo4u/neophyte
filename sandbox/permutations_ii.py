class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.bt(nums, len(nums), 0, [])

    def bt(self, nums, n, start, result):
        if start == n - 1:
            result.append(nums.copy())
            return result
        used = set()

        for i in range(start, n):
            if nums[i] in used: continue
            used.add(nums[i])
            if i != start: nums[i], nums[start] = nums[start], nums[i]
            self.bt(nums, n, start + 1, result)
            if i != start: nums[i], nums[start] = nums[start], nums[i]

        return result


# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/description/


# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

sol = Solution()
assert sol.permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

