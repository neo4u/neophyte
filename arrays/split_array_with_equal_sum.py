class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7: return False

        pre_sum = [nums[0]] + [0] * n
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + nums[i]

        for j in range(3, n - 3):
            l_sums = set()
            for i in range(1, j - 1):
                if pre_sum[i - 1] == pre_sum[j - 1] - pre_sum[i]:
                    l_sums.add(pre_sum[i - 1])

            if not l_sums: continue

            for k in range(j + 2, n - 1):
                r_part = pre_sum[n - 1] - pre_sum[k]
                if pre_sum[k - 1] - pre_sum[j] == r_part and r_part in l_sums:
                    return True

        return False


# 548. Split Array with Equal Sum
# https://leetcode.com/problems/split-array-with-equal-sum/description/


# Optimal Approach: Hash Set + Cumulative Sum

# 1. Choose a mid split point j starting from 2 upto n - 4 [2, n - 3]
# 2. Try every left split point i ranging from 1 to j - 2 [1, j - 1]
# 3. Once you find split point such that 1st part sum == 2nd part sum
# 4. Try every possible right split point ranging from j + 2 to n - 2 [j + 2, n - 1]
# 5. If 3rd part == 4th part and the sum is in the hash set then return true
# 6. Else return false

# Time: O(n^2), One outer loop and two inner loops are used.
# Space: O(n), HashSet size can go upto n.
