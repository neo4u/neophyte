from typing import List

# Approach 0: Top Down Recursion
# A. Using lru_cache
import functools
class Solution0A:
    @functools.lru_cache(maxsize=None)
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k: return []
        if k == 1: return [[num] for num in range(1, n + 1)]

        ans = []

        for i in range(k, n + 1):                               # determine the largest number in combination, say, i
            ans += [combo + [i] for combo in self.combine(i - 1, k - 1)]

        return ans

# B. Without using lru_cache
class Solution0B:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n: return []
        if k == 1: return [[i + 1] for i in range(n)]

        combine_less = []
        res = []

        for i in range(1, n - k + 2):
            combine_less = self.combine(n - i, k - 1)
            res += [c + [n - i + 1] for c in combine_less]

        return res

# C. Using itertools
from itertools import combinations
class Solution0C(object):
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        for c in combinations([i for i in range(1, n + 1)], k):
            res.append(list(c))

        return res

# Approach 1: Classic Backtracking
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.output = []
        self.bt(n, k, 1, [])
        return self.output

    def bt(self, n, k, s_idx, path):
        if len(path) == k: return self.output.append(path[:])   # Prune paths at the point where path len reaches k

        for i in range(s_idx, n + 1):
            path.append(i)                              # add i into the current combination
            self.bt(n, k, i + 1, path)                  # use next integers to complete the combination
            path.pop()                                  # backtrack


# Approach 1: Classic BT with slight change by passing the copy to next level BT call
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.nums = list(range(1, n + 1))
        self.bt(k, 0, [])
        return self.result

    def bt(self, k, s_idx, path):
        if len(path) == k: self.result.append(path)
        for i in range(s_idx, len(self.nums)): self.bt(k, i + 1, path + [self.nums[i]])


# Approach 2: Lexicographic (Binary Sorted) Combinations (Optimal)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, k + 1)) + [n + 1]              # init first combination

        output, j = [], 0
        while j < k:
            output.append(nums[:k])                         # add current combination

            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:     # increase first nums[j] by one
                nums[j] = j + 1                             # if nums[j] + 1 != nums[j + 1]
                j += 1

            nums[j] += 1

        return output



# 77. Combinations
# https://leetcode.com/problems/combinations/description/


# Approach 0: Top Down Recursion
# A. Using lru_cache
# B. Without lru_cache
# C. Using itertools.combinations

# Approach 1: Classic Backtracking
# Steps:
# 1. Keep a global (self.result) to hold all combinations and a local to hold the current combination (path)
# 2. Call the base case with an empty path and start integer 1 [self.bt(n, k, 1, [])], this will be the root of the tree
# 3. We use the len of the path as the base case and append the path to result and return in such a case
# 4. In all other cases, we do two things:
#    - self.bt method iterates from [start to n] and appends the integer to path
#    - it then calls the next level of recursion with a copy of the current path that can be modified along the path

# Time: O(k * nCk)
# Space: O(nCk)

# Approach 2: Lexicographic (Binary Sorted) Combinations
# Steps:
# 1. Generate the first sequence and add a sentinal at the end
# 2. Try to 
# 3. 

# Example: n = 4, k = 2
#         output: [[1, 2, 3]], nums: [1, 2, 3, 5], j: 1
#         output: [[1, 2, 3]], nums: [1, 2, 3, 5], j: 2
# output: [[1, 2, 3]], nums: [1, 2, 4, 5], j: 2
#         output: [[1, 2, 3], [1, 2, 4]], nums: [1, 2, 4, 5], j: 1
# output: [[1, 2, 3], [1, 2, 4]], nums: [1, 3, 4, 5], j: 1
# output: [[1, 2, 3], [1, 2, 4], [1, 3, 4]], nums: [2, 3, 4, 5], j: 0
#         output: [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], nums: [1, 3, 4, 5], j: 1
#         output: [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], nums: [1, 2, 4, 5], j: 2
#         output: [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], nums: [1, 2, 3, 5], j: 3
# output: [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], nums: [1, 2, 3, 6], j: 3

# Time: O(k * nCk)
# Space: O(nCk)



# n = 4, k = 3
# 1 combine with [2, 3], [3, 4], [2,4] gives us 3 results
# 1, 2, 3
# 1, 3, 4

# 2 combine with [3, 4],          gives us 1 results
# 2, 3, 4


sol0A = Solution0A()
assert sol0A.combine(4, 3) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
assert sol0A.combine(4, 2) == [[1, 2], [1, 3], [2, 3], [1, 4], [2, 4], [3, 4]]

sol0B = Solution0B()
assert sorted(sol0B.combine(4, 3)) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
assert sorted(sol0B.combine(4, 2)) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

sol0C = Solution0C()
assert sorted(sol0C.combine(4, 3)) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
assert sorted(sol0C.combine(4, 2)) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

sol1 = Solution1()
assert sorted(sol1.combine(4, 3)) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
assert sorted(sol1.combine(4, 2)) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

sol = Solution()
assert sorted(sol.combine(4, 3)) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
# assert sorted(sol.combine(4, 2)) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
