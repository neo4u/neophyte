from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_map, pre_sum = {0: -1}, 0

        for r, num in enumerate(nums):
            pre_sum += num
            if k != 0: pre_sum %= k

            if pre_sum in sum_map:
                l = sum_map[pre_sum]
                if r - l >= 2: return True
            else:
                sum_map[pre_sum] = r

        return False



# 523. Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/


# Intuition:
# 1. If pre_sum %= k was seen before, it means the sum of the array
#    between the previous time the pre_sum was seen and curr pre_sum is a multiple of k.
# 2. difference in indexes gives the size of the array.

# 523. Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

# Approach 1: Brute-force, Time: O(n^3), Space: O(1)

# Approach 2: Brute-force with cumulative sum array, Time: O(n^2), Space: O(n)

# Approach 3: Hash-map with cumulative sum % k (k != 0), Time: O(n), Space: O(min(n, k))

# Steps:
# 1. Maintain a hash map with cumulative sum % k as keys and current index as value
# 2. Iterate through hash and keep adding current pre_sum  %= k to the hash with value as the index of that pre_sum
# 3. If pre_sum in map, it means we already had a previous sum that had the same remainder on division with k
# 4. Thus if the difference is indices is >= 2, then we've found such a sub-array who sum is a multiple of k
#    hence, return true.

# why do we insert key, value pair 0, -1 at the start into map
# Consider that the first element itself is the sub-array sum multiple of k
# Example 1: [2, 3, 4], k = 2
# i = 0, pre_sum = 2, pre_sum % k = 0,
# Our hash so far is: { 0 => -1 }
# 0 is found in the hash, so we check if i - map[pre_sum] >= 2
# 0 - (-1) == 1 which is not >= 2, so we have to move on

# i = 1, pre_sum = 0 + 3 == 3, pre_sum % k = 1
# we add to map => { 0 => -1, 1 => 1}, we move on

# i = 2, pre_sum = 1 + 4 == 5, pre_sum % k = 1
# we have that in our map so, we check if i - map[i] >= 2
# 2 - 1 == 1 which is not >= 2, hence we're done and return false
# And thsu we find that there is no such continuous subarray sum.


# Example 2: [23, 2, 4, 6, 7], k = 6
# r = 0
# pre_sum = 23, pre_sum % k = 5
# sum_map = {0: -1, 5: 0}

# r = 1
# pre_sum = 7, pre_sum % k = 1
# sum_map = {0: -1, 5: 0, 1: 1}

# r = 2
# pre_sum = 1 + 4 = 5 % 6 = 5
# Since we've seen 5 before and and since r - l => 2 - 0 => 2
# we return True

#
# if we didn't, have the 0 and -1 added to the map
# consider the corner cases:
# nums, k
# [0], 0        -> false. Map would be {0 => -1}, 0 - -1 == 1 not >= 2 causes us to return false
# [5, 2, 4], 5  -> false. Map would be {0 => -1, 2 => 1, 1 => 2}. Thus never returning true
# [0, 0], 100   -> true, Map would be {0 => -1}, but when i = 1, i - map[pre_sum%k] == 1 - -1 == 2, thus we return true
# [1,5], -6     -> true, Map would be {0 => -1, -5 => 0}, then at i = 1, we get pre_sum % k = -5 + 5 == 0 % -6 == 0, thus 1 - -1 == 2

# Optimal:
# Time: O(n). Only one traversal of the array nums is done.
# Space: O(min(n,k)). The HashMap can contain upto min(n,k) different pairings.


sol = Solution()
assert sol.checkSubarraySum([0, 0], 0) == True
assert sol.checkSubarraySum([2, 3, 4], 2) == False
assert sol.checkSubarraySum([1, 5], -6) == True
assert sol.checkSubarraySum([0, 0], 100) == True
assert sol.checkSubarraySum([0], 0) == False
assert sol.checkSubarraySum([5, 2, 4], 5) == False
