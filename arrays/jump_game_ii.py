class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps, curr_end, curr_farthest = 0, 0, 0

        for i in range(n - 1):
            curr_farthest = max(curr_farthest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = curr_farthest

        return jumps


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        if set(nums) == {1}: return len(nums) - 1

        endpoint = len(nums) - 1
        while endpoint != 0:
            for i in range(endpoint):
                if nums[i] + i >= endpoint:
                    jumps += 1
                    endpoint = i
                    break

        return jumps
