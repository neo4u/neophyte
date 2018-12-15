class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        index = range(length)
        self.count = [0] * length
        self.mergesort(nums, index, 0, length)
        return self.count

    def mergesort(self, nums, index, lo, hi):
        if lo >= hi - 1:
            return
        mid = (lo + hi) // 2
        self.mergesort(nums, index, lo, mid)
        self.mergesort(nums, index, mid, hi)
        self.merge(nums, index, lo, hi)
        
    def merge(self, nums, index, lo, hi):
        mid = (lo + hi) // 2
        i, j = lo, mid
        rightcount = 0
        new_index = []
        while i < mid and j < hi:
            if nums[index[i]] > nums[index[j]]:
                new_index.append(index[j])
                rightcount += 1
                j += 1
            else:
                new_index.append(index[i])
                self.count[index[i]] += rightcount
                i += 1
        while i < mid:
            self.count[index[i]] += rightcount
            new_index.append(index[i])
            i += 1
        while j < hi:
            new_index.append(index[j])
            j += 1
        
        index[lo:hi] = new_index
