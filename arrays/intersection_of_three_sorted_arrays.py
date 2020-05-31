from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i = j = k = 0
        result = []

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i, j, k = i + 1, j + 1, k + 1
                continue

            max_ = max(arr1[i], arr2[j], arr3[k])
            i = i + 1 if arr1[i] < max_ else i
            j = j + 1 if arr2[j] < max_ else j
            k = k + 1 if arr3[k] < max_ else k

        return result


# 1213. Intersection of Three Sorted Arrays
# https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/
