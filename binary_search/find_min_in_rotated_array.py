class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if middle - 1 >= left and nums[middle] < nums[middle - 1]:
                return nums[middle]
            
            if nums[middle] < nums[left]:
                right = middle - 1
            elif nums[middle] > nums[right]:
                left = middle + 1
            else:
                return nums[left]

solution = Solution()
assert solution.findMin([3,4,5,1,2]) == 1