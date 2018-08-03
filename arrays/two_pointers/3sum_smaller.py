class Solution(object):
	def threeSumSmaller(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		n = len(nums)
		count = 0
		nums.sort()
		for i in range(n - 2): # Skip last two because next loop iterates through them
			s = target - nums[i]
			l, r = i + 1, n - 1

			while l < r:
				if nums[l] + nums[r] >= s:
					r -= 1
				else:
					count += r - l
					l += 1

		return count

sol = Solution()
assert sol.threeSumSmaller([-2,0,1,3], 2) == 2