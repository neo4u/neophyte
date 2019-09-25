class Solution:
    def combinations(nums: List[int], k: int):
        self.result = []
        self.bt(nums, k, start)
        return self.result

    def 