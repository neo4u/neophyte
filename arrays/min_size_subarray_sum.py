# O(n)
class Solution:

    def minSubArrayLen(self, s, nums):
        total = l = 0
        result = len(nums) + 1

        for r, n in enumerate(nums):
            total += n

            while total >= s:
                result = min(result, r - l + 1)
                total -= nums[l]
                l += 1

        return result if result <= len(nums) else 0


# O(nlog(n))
class Solution(object):
    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1

        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n

        l = 0
        for r, n in enumerate(nums):
            if n >= target:
                l = self.find_left(l, r, nums, target, n)
                result = min(result, r - l + 1)

        return result if result <= len(nums) else 0

    def find_left(self, l, r, nums, target, n):
        while l < r:
            mid = (l + r) // 2
            if n - nums[mid] >= target:
                l = mid + 1
            else:
                r = mid

        return l