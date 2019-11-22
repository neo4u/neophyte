from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Best single, double, and triple sequence found so far
        n = len(nums)
        best_1_seq, best_2_seq, best_3_seq = 0, [0, k], [0, k, k*2]

        # Sums of each window
        seq_1_sum, seq_2_sum, seq_3_sum = sum(nums[0:k]), sum(nums[k:k*2]), sum(nums[k*2:k*3])

        # Sums of combined best windows
        best_1_sum = seq_1_sum
        best_2_sum = seq_1_sum + seq_2_sum
        best_3_sum = seq_1_sum + seq_2_sum + seq_3_sum

        # Start loop with 1 pos after curr windows
        seq_1_i = 1; seq_2_i = k + 1; seq_3_i = k*2 + 1

        while seq_3_i <= n - k:
            out_1, in_1 = nums[seq_1_i - 1], nums[seq_1_i + k - 1]
            out_2, in_2 = nums[seq_2_i - 1], nums[seq_2_i + k - 1]
            out_3, in_3 = nums[seq_3_i - 1], nums[seq_3_i + k - 1]

            # Update the three sliding window sums
            seq_1_sum = seq_1_sum - out_1 + in_1
            seq_2_sum = seq_2_sum - out_2 + in_2
            seq_3_sum = seq_3_sum - out_3 + in_3

            # Update best single window
            if seq_1_sum > best_1_sum:
                best_1_sum = seq_1_sum
                best_1_seq = seq_1_i

            # Update best two windows
            if seq_2_sum + best_1_sum > best_2_sum:
                best_2_sum = seq_2_sum + best_1_sum
                best_2_seq = [best_1_seq, seq_2_i]

            # Update best three windows
            if seq_3_sum + best_2_sum > best_3_sum:
                best_3_sum = seq_3_sum + best_2_sum
                best_3_seq = best_2_seq + [seq_3_i]

            # Update the current positions
            seq_1_i += 1; seq_2_i += 1; seq_3_i += 1

        return best_3_seq


# 689. Maximum Sum of 3 Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

# A greedy solution using three sliding windows where you keep track of the best indexes/sums as you go.

# O(n) time: Since we're only going through the list once and using no complex operations, this is O(n).
# O(1) space: Just a fixed set of temp vars. We don't need the extra arrays that the DP solutions have.



# Steps:
# 1. Start windows with 1st k, 2nd k, and 3rd k
# 2. Keep moving each one and recording the indexes of the best sum windows

# Time: O(n), one traversal of list
# Space: O(1)

sol = Solution()

assert sol.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2) == [0, 3, 5]
assert sol.maxSumOfThreeSubarrays([7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3) == [1, 4, 7]
assert sol.maxSumOfThreeSubarrays([4, 5, 10, 6, 11, 17, 4, 11, 1, 3], 1) == [4, 5, 7]
