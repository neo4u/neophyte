class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.pre_sum = [0] * (len(nums) + 1)
        for i, n in enumerate(self.nums):
            self.pre_sum[i + 1] = self.pre_sum[i] + nums[i]

    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        for j in range(i + 1, self.n):
            self.pre_sum[j] += delta
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.pre_sum[j + 1] - self.pre_sum[i]
