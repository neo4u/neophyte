class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.updatedlist = []
        self.updateList()
    
    def updateList(self):
        if len(self.nums) >0:
            self.updatedlist.append(self.nums[0])
        for i in range(1,len(self.nums)):
            self.updatedlist.append(self.updatedlist[i-1] + self.nums[i])


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = self.updatedlist[j]
        if i >=1:
            sum -= self.updatedlist[i-1]
        return sum