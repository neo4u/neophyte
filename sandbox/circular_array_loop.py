class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            # use a distinct marker for each starting point
            mark = str(i)
            
            # explore while node is new, direction is same, and is not self loop
            # note: if node has been marked by a different marker, no need to proceed. This gives O(n) time.
            while (type(nums[i]) == int) and (num * nums[i] > 0) and (nums[i] % len(nums) != 0):
                jump = nums[i] 
                nums[i] = mark
                i = (i + jump) % len(nums)
            
            # if self loop, nums[i] is never marked
            # if nums[i] is marked, a cycle is found
            if nums[i] == mark:
                return True
            
        return False

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2: return False
        n = len(nums)

        for i in range(n):
            if type(nums[i]) != int: continue # visited element
            if nums[i] % n == 0: continue # self-loop
            direction = (nums[i] > 0) # loop direction, cannot be changed midway

            mark = str(i)
            while (type(nums[i]) == int) and (direction == (nums[i] > 0)) and (nums[i] % n != 0):
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % n

            if nums[i] == mark: return True

        return False