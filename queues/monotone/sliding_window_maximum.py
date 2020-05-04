from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0: return []                    # base cases not needed but add's value in interview
        if k == 1: return nums
        q, result = collections.deque(), []         # 'result' is for storing n - k + 1 results

        for i, num in enumerate(nums):
            if q and q[0][1] + k <= i: q.popleft()  # remove 1 from left
            while q and q[-1][0] < num: q.pop()     # pop until num we find an element > num, thus ensuring monotone dec
            q.append((num, i))                      # Append to monotonically decreasing queue
            if i >= k - 1: result.append(q[0][0])   # We start our appending of result from k - 1, which is the end of first window

        return result


# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/description/

# Time: O(n)
# Space: O(n)

sol = Solution()
assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
