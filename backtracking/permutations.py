from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.n = len(nums)
        self.bt(nums, 0)
        return self.result

    def bt(self, nums, fixed):
        if fixed == self.n - 1: return self.result.append(nums.copy())

        for i in range(fixed, self.n):
            if fixed != i: self.swap(nums, fixed, i)
            self.bt(nums, fixed + 1)
            if fixed != i: self.swap(nums, fixed, i)

    @staticmethod
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


# 46. Permutations
# https://leetcode.com/problems/permutations/description/

# Steps:
# 1. We use a 'result' list to hold all the permutations
# 2. We start the recursion from index 0 (This will be our initial fixed index),
#    we swap elements at every index with the element at index start
# 3. Once we swap we call the next recursion level and increment the fixed index by one
# 4. In the recursion at any time if our fixed index reach n - 1,
#    then we add the permutation to result

# Example: nums = [1, 2, 3]
# bt(0, [1 2 3])
#     bt(1, [1,2,3])
#         bt(2, [1,2,3])
#            bt(3, [1,2,3]) results = [[1,2,3]]
#            ret
#         bt(2, [1,3,2])
#             bt(3, [1,3,2]) results = [[1,2,3], [1,3,2]]
#             ret
#     bt(1, [2,1,3])
#         bt(2, [2,1,3])
#             bt(3, [2,1,3]) results = [[1,2,3], [1,3,2], [2,1,3]]
#             ret
#         bt(2, [2,3,1])
#             bt(3, [2,3,1]) results = [[1,2,3], [1,3,2], [2,1,3], [2,3,1]]
#             ret
#     bt(1, [3,2,1])
#         bt(2, [3,2,1])
#             bt(3, [3,2,1]) results = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1]]
#             ret
#         bt(2, [3,1,2])
#             bt(3, [3,1,2]) results = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]
#             ret

# Time: O(sum(nPk)) for k = 1...n,
# where P(n, k) = n!/(n − k)! = n (n − 1)...(n − k + 1) is so-called k-permutations_of_n, or partial permutation
# which is <= n * n!
# thus the algorithm performs better than O(n * n!) and a bit slower than O(n!).
# Space: O(n!)


sol = Solution()
assert sol.permute([1, 2, 3]) == [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 2, 1],
    [3, 1, 2]
]
assert sol.permute([1, 2]) == [[1, 2], [2, 1]]
