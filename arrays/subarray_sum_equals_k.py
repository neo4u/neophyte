# Brute Force (TLE), Time: O(N^3), Space: O(1)
# For every sub-array calculate the sub-array sum and count how many of them == k
class Solution:
    def subarraySum(self, nums, k):
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j+1]) == k:
                    res += 1
        return res

# PrefixSum (TLE), Time: O(N^2), Space: O(1)
# 1. Calculate sum of all elements upto nums[i] for every i in array
# 2. if prefix sum is already k add to result
# 3. from i to j if sum at j - sum at i is k that means sub-array nums[i to j] had sum k
class Solution:
    def subarraySum(self, nums, k):
        res = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        for i in range(len(nums)):
            if nums[i] == k: res += 1
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] == k: count += 1

        return res

# PrefixSum + Dictionary, Time: O(N), Space: O(N)
class Solution:
    def subarraySum(self, nums, k):
        dic = {0:1}
        res = pre_sum = 0
        for num in nums:
            pre_sum += num
            res += dic.get(pre_sum - k, 0)
            dic[pre_sum] = dic.get(pre_sum, 0) + 1
        return res

# Let's remember count[V], the number of previous prefix sums with value V.
# If our newest prefix sum has value W, and W-V == K, then we add count[V] to our answer.
# This is because at time t, A[0] + A[1] + ... + A[t-1] = W,
# and there are count[V] indices j with j < t-1 and A[0] + A[1] + ... + A[j] = V.
# Thus, there are count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.
def subarraySum(self, nums, k):
        count, cur, res = {0: 1}, 0, 0
        for v in nums:
            cur += vcount.get(cur, 0)
            res += count.get(cur - k, 0)
            count[cur] =  + 1
        return res

# Complexity Analysis
# Time complexity: O(n). The entire nums array is traversed only once.
# Space complexity: O(n). Hashmap mapmap can contain upto nn distinct entries in the worst case.
