class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0
        diff = nums[-1] - nums[0] + 1 # complete length
        missing = diff - len(nums) # complete length - real length

        if k > missing: # if k is larger than the number of mssing words in sequence
            return nums[-1] + k - missing

        l, r = 0, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) // 2
            missing = nums[mid] - nums[l] - (mid - l)
            if missing < k:
                l = mid
                k -= missing # KEY: move left forward, we need to minus the missing words of this range
            else:
                r = mid
        return nums[l] + k # k should be between left and right index in the end


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
        n = len(nums)
        # If kth missing number is larger than
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        l, r = 0, n - 1
        # find left = right index such that
        # missing(left - 1) < k <= missing(left)
        while l != r:
            pivot = l + (r - l) // 2
            if missing(pivot) < k:  l = pivot + 1
            else:                   r = pivot

        # kth missing number is greater than nums[left - 1]
        # and less than nums[left]
        return nums[l - 1] + k - missing(l - 1) 


# 1060. Missing Element in Sorted Array
# https://leetcode.com/problems/missing-element-in-sorted-array/description/


# 0 n - 1

# 3, 2, 1,4,7

# 0, 1, 2, 3, 4
# 1, 2, 3, 4, 7

# 4 - 1 - i

# [1, 10], k = 20
# [0, 8]

# 4, 7, 9, 10, 50], k = 20
# [0, 2, 3,  3, 52]
