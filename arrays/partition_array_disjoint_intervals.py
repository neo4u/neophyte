from typing import List


# Approach 1: Aux array
class Solution1:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        max_l, min_r = [None] * n, [None] * n

        m = A[0]
        for i in range(n):
            if A[i] > m: m = A[i]
            max_l[i] = m

        m = A[-1]
        for i in range(n - 1, -1, -1):
            if A[i] < m: m = A[i]
            min_r[i] = m

        for i in range(1, n):
            if max_l[i - 1] <= min_r[i]:
                return i


# Approach 2: 2 Pass with 1 Aux
class Solution2:
    def partitionDisjoint(self, A):
        n = len(A)
        min_r = [A[-1]] * n

        for i in range(n - 2, -1, -1):
            min_r[i] = min(min_r[i + 1], A[i])

        max_l = -float('inf')
        for i in range(1, n):
            max_l = max(max_l, A[i - 1])
            if max_l <= min_r[i]:
                return i


# Approach 3: 1 Pass, (Sorta like a 2/3-way partitioning algorithm)
class Solution:
    def partitionDisjoint(self, A):
        p_idx = 0
        g_max = l_max = A[0]

        for i, num in enumerate(A):
            if l_max > num:     # Entire sub-arrary thusfar becomes left partition, hence curr_max becomes the l_max
                l_max = g_max
                p_idx = i
            else:
                g_max = max(g_max, num)
        return p_idx + 1



# 915. Partition Array into Disjoint Intervals
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/


# Intuition:
# 1. The paritioning should be contiguous, which means you get 1 cut between any indexes
# 2. Everything in the left array should be less than the elements in the right
# 3. The above stmt is equivalent to saying that max(left_part) < min(right_part)


# Approach 1: Aux Array
# - Use aux arrays max_l and min_r
# - max_l[i] represents the index of the max element of all the nums to nums[i]'s left
#   we set this using a linear scan and keeping a running max
# - min_r[i] represents the index of the min element of all the nums to nums[i]'s right
# - We scan the indexes i from 1 to n - 1 and compare elements at i - 1 and i
#   and return when we notice the 3rd condition from intuition

# Time: O(n)
# Space: O(n)

# Approach 2: 2-Pass with 1 Aux
# Skip the first maxleft pass, keep only the min_r array, and use max_l as a variable

# Time: O(n)
# Space: O(n)

# Approach 3: 1 Pass, (Sorta like a 2/3-way partitioning algorithm)
# Use one more variable l_max to moniter


#  The process divides the array to 3 partitions:
#  A[0]...A[p_idx] | A[p_idx + 1]...A[j]...A[i - 1] | A[i]...A[n - 1]
#                                                     ^
#                                                     | current visiting
#  [0, p_idx] is the left partition
#  [p_idx + 1, i - 1] is the second partition
#  [i, n - 1] is the last partition, which is to be processed.

#  all elements from second partition are great or equal to the first partition's max.
#  we maintain two max:
#  l_max: the max value for first partition [0->p_idx]
#  curr_max: the max value for all elements we already visited [0, i]
#  p_idx is index to partition the subarray A[0, i - 1]

# now if l_max > A[i], it means should re-partition subarray A[0, i], with i as the p_idx,
# and assign curr_max to l_max, because now the first partition became: [0, i].
# else
# we just update curr_max and continue


# Time: O(n)
# Space: O(1)


sol = Solution1()
assert sol.partitionDisjoint([5, 0, 3, 8, 6]) == 3
assert sol.partitionDisjoint([1, 1, 1, 0, 6, 12]) == 4

sol = Solution2()
assert sol.partitionDisjoint([5, 0, 3, 8, 6]) == 3
assert sol.partitionDisjoint([1, 1, 1, 0, 6, 12]) == 4

sol = Solution()
assert sol.partitionDisjoint([5, 0, 3, 8, 6]) == 3
assert sol.partitionDisjoint([1, 1, 1, 0, 6, 12]) == 4
