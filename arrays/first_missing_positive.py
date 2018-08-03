import sys

class Solution:
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		numbers = {i : 1 for i in nums}
		for i in range(1, sys.maxsize, 1):
			if not i in numbers:
				return i

		return sys.maxsize