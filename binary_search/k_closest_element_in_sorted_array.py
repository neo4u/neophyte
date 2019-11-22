from typing import List
from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[-k:]
        else:
            l, r = 0, len(arr) - k

            while l < r:
                mid = (l + r) // 2

                if abs(arr[mid + k] - x) < abs(arr[mid] - x):
                    l = mid + 1
                else:
                    r = mid

        return arr[l : l + k]


# 658. Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/description/


# [1,2,3,4,5,9,10]
#  l
#  r

# k=4, target=3
# l = 0, r = 3
# mid = 1


# l 0, r = 1
# mid = 0
