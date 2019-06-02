class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_sum = [0] * (len(nums) + 1)
        for i, n in enumerate(self.nums):
            self.pre_sum[i + 1] = self.pre_sum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.pre_sum[j + 1] - self.pre_sum[i]


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        for i, n in enumerate(1, self.nums):
            self.nums[i] += self.nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if not i:
            return self.nums[j]
        return self.nums[j] - self.nums[i - 1]


]


1 2 3 3 5
1 3 6 9 14

i j 

i j + 1