from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        self.result = []
        self.bt(nums, 0, [])
        return self.result

    def bt(self, nums: List[int], s_idx: List[int], path: List[int]):
        self.result.append(path)
        if s_idx == len(nums): return

        for i in range(s_idx, len(nums)):
            self.bt(nums, i + 1, path + [nums[i]])


# 78. Subsets
# https://leetcode.com/problems/subsets/description/

# [1,2,3]
# bt(0,[])
#     bt(1, [1])
#         bt(2,[1,2])
#             bt(3, [1,2,3])
#             return
#         return
#         bt(3,[1,3])
#         return
#     bt(2,[2])
#         bt(3,[2,3])
#         return
#     return
#     bt(3,[3])
#     return

#   { [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3] }
