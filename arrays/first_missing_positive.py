from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 0 <= nums[i] - 1 <= n - 1 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1: return i + 1

        return n + 1


# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/description/

# Inuition
# 1. We need to find the first positive number that is missing.
# 2. The question could be twisted to make the range of numbers in the array 0...N-1 or 1 to N

# Steps:
# 1. We're going to iteratively visit each number in the array, and in turn form an index out of that number
#    i.e. if we have nums[i] is x, then we're going to see what is the number at nums[x - 1],
#    making x - 1 the index using x
# 2. We're going to loop as long as:
#    - The element at the current index i forms a valid index i.e. 0 <= nums[i] - 1 <= n - 1 and
#    - The number at the index formed by the current number (nums[nums[i] - 1]) is not already nums[i]
#      i.e. as long as the number supposed to be in that index is not already in that index, keep swapping it out with nums[i]
# 3. Once this is done for all the elements, we just find the first index i for which nums[i] != i + 1
#    and we return i + 1, that is the number formed by the index
# 4. Final piece is that, if all the numbers are in their appropriate indexes, then n + 1 is the missing number

# Time: O(n)
# Space: O(1)

# Some points to ponder:
# 1. Is 0 +ve or -ve? It is both, so if it is missing what are we supposed to do?
#    Based on this example: Input: [3,4,-1,1], Output: 2
#    We ignore 0 if it is missing,
#    this example after swapping leads to: [1, -1, 3, 4]
#    First missing integer is 2 which is the answer and not zero
# 2. What if there are duplicates?
#    no problem, our method should still work
#    Example: [1, 2, 2, 1, 3, 1, 0, 4, 0] should lead to [1, 2, 3, 4, 2, 1, 0, 1, 0] after the swaps
#    leading to an answer of 5, all the duplicates, -ves, and zeroes get pushed to the back
#    The answer would've been 5 even if the input was: [1, 2, 2, -1, 3, -1, 0, 4, 0]
#    Because after swaps we would get: [1, 2, 3, 4, 2, -1, 0, -1, 0] leading to an answer of 5
# 3. What if there are negative numbers?
#    Answered above, solution still would work, it'll just lead to bad indexes and thus get swapped out to the back
# 4. Is the complexity O(n)? While O(n) inside a for O(n) shudn't it be O(n ^ 2),
#    No. because, it is not O(n) inside O(n), it is O(n) for the outer,
#    but the inside loop totals to n, and doesn't do O(n) for each iteration
#    Bcuz, Once an element reaches its place or forms a bad index, we don't enter the loop for those elements


sol = Solution()

assert sol.firstMissingPositive([1, 2, 0]) == 3
assert sol.firstMissingPositive([3, 4, -1, 1]) == 2
assert sol.firstMissingPositive([7, 8, 9, 11, 12]) == 1
assert sol.firstMissingPositive([1, 2, 2, -1, 3, -1, 0, 4, 0]) == 5
