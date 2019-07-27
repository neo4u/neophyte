from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result, stack = [-1] * n, [] 

        for i in list(range(n)) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)

        return result


# 503. Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/description/



# https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6

# https://leetcode.com/problems/sliding-window-maximum/discuss/65885/this-is-a-typical-monotonic-queue-problem

# Can be also used to solve:
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# https://leetcode.com/problems/next-greater-element-i/
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
