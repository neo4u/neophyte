from typing import List


# Approach 1: With sort and without set
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        self.result = []
        self.bt(nums, 0, [])
        return self.result

    def bt(self, nums: List[int], s_idx: int, path: List[int]) -> None:
        self.result.append(path)

        used = set()
        for i in range(s_idx, len(nums)):
            if nums[i] in used: continue
            used.add(nums[i])
            self.bt(nums, i + 1, path + [nums[i]])


# Approach 2: With sort and set for used numbers
class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.bt(nums, 0, [])
        return self.result

    def bt(self, nums: List[int], s_idx: int, path: List[int]) -> None:
        self.result.append(path)
        if s_idx == len(nums): return

        for i in range(s_idx, len(nums)):
            if i > s_idx and nums[i] == nums[i - 1]: continue
            self.bt(nums, i + 1, path + [nums[i]])


# Approach 3: Using the number and frequency
import collections
class Solution3:
    def subsetsWithDup(self, nums):
        result = [[]]

        for num, freq in collections.Counter(nums).items():
            tmp_result = []
            for i in range(1, freq + 1):
                tmp_result += [r + [num] * i for r in result]
            result += tmp_result

        return result

# 1 4 5 4

# bt(1, [1])
#     bt(2, [1 4])
#         i 2 to 3
#         bt(3, [1 4 5])
#             bt(4, [1 4 5 4])
#             ret
#         ret
#         bt(4, [1 4 4])
#     bt(3, [1, 5])
#         bt(4, [1, 5, 4])

# 1 4 4 5
# bt(1, [1])
#     bt(2, [1 4])
#         i 2 to 3
#         bt(3, [1 4 4])
#             bt(4, [1 4 4 5])
#             ret
#         ret
#         bt(4, [1 4 5])
#         ret
#     ret
#     x - bt(3, [1, 4])
#     bt(4, [1, 5])


# [1,2,2]

# bt(0, [])
#     i 0 to 2
#     bt(1, [1])
#         i 1 to 2
#         bt(2, [1, 2])
#     bt(2, [2])
#         bt(3, [2, 2])


# 1 2 3

# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# 1 2 2


# 1 2 3

# 1 2
# 1 3
# 2 3


# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/description/
