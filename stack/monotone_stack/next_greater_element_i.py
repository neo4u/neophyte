from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater, stack = {}, []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        return list(map(lambda x: next_greater.get(x, -1), nums1))



# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/description/




# https://medium.com/algorithms-and-leetcode/monotonic-queue-explained-with-leetcode-problems-7db7c530c1d6

# https://leetcode.com/problems/sliding-window-maximum/discuss/65885/this-is-a-typical-monotonic-queue-problem

# Can be also used to solve:
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# https://leetcode.com/problems/next-greater-element-i/
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# https://leetcode.com/problems/sum-of-subarray-minimums/description/
# https://leetcode.com/problems/odd-even-jump/description/
