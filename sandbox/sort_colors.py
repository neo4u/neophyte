class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        curr = 0

        while curr <= r:
            if nums[curr] == 0:
                nums[l], nums[curr] = nums[curr], nums[l]
                curr += 1; l += 1
            elif nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
            else:
                curr += 1





# 1 1 1 2 2 2 curr 234234234 2 3 3 3 3 
# 0 2    0 2
#   cur  r
#   l

#           unknown
#        ___________________________
# 0 0 0 1 2 0 1 0 1 0 2 0 2 0 1 0 2 2
#        l                         r
#        c

#                      unknown
#                 _______________________
# 0 0 0 1 1 1 1 1 2 0 1 0 1 0 2 0 2 0 1 0 2 2
#       l         c                     r
