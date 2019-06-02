class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] < nums[r]: return nums[l]
                
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

# [4,5,6,7,0,1,2]


# [1,2,3,4,5,6]
# [2,3,4,5,6,1,]


# (i.e.,  [0,1,2,4,5,6,7] might become  ).
#         [6,7,0,1,2,4,5] - 1


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        if nums[r] > nums[0]:
            return nums[0]

        while l <= r:
            mid = l + (r - l) / 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
