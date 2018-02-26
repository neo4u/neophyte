class Solution:
  # @return an integer
	def lengthOfLongestSubstring(self, s):
		used = {}
		max_length = start = 0
		for i, c in enumerate(s):
			if c in used and start <= used[c]:
				start = used[c] + 1
			else:
				max_length = max(max_length, i - start + 1)
			used[c] = i
		return max_length

solution = Solution()

assert solution.lengthOfLongestSubstring("abcabcbb") == 3
assert solution.lengthOfLongestSubstring("bbbbb") == 1
assert solution.lengthOfLongestSubstring("pwwkew") == 3
