from typing import List


# Solution 1:
# use set operation in python, one-line solution.
class Solution(object):
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# Solution 2:
# brute-force searching, search each element of the first list in the second list. (to be more efficient, you can sort the second list and use binary search to accelerate)
class Solution(object):
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)

        return res

# Solution 3:
# use dict/hashmap to record all nums appeared in the first list, and then check if there are nums in the second list have appeared in the map.
class Solution(object):
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        map = {}
        for i in nums1:
            map[i] += 1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0
        return res

# Solution 4:
# sort the two list, and use two pointer to search in the lists to find common elements.
class Solution(object):
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        m, n, i, j = len(nums1), len(nums2), 0, 0
        nums1.sort(); nums2.sort()

        while i < m and j < n:
            if nums1[i] > nums2[j]:     j += 1
            elif nums1[i] < nums2[j]:   i += 1
            else:
                if not result or nums1[i] != result[-1]:
                    result.append(nums1[i])
                i += 1; j += 1

        return result


import collections
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2, result = sorted(nums1), sorted(nums2), []

        while nums1 and nums2:
            while len(nums1) > 1 and nums1[0] == nums1[1]: nums1.pop(0) # Skip duplicates
            while len(nums2) > 1 and nums2[0] == nums2[1]: nums2.pop(0) # Skip duplicates
            top1, top2 = nums1[0], nums2[0]

            if top1 < top2:   nums1.pop(0)
            elif top2 < top1: nums2.pop(0)
            else:
                result.append(top1)
                nums1.pop(0); nums2.pop(0)

        return result


# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

# Note worthy points
# Each element in the result must be unique.
# The result can be in any order.

# Approaches
# Where n is the combined length of both arrays
# Approach 1: Using two sets Time: O(n) Space: O(n)
# Approach 2: Using a hash, Time: O(n) Space: O(n)
# Approach 3: Binary search, iterate through one and sort and do bi nary search on the other, Time: O(nlog(n)), Space: O(1)
# Approach 4: Two pointer (java) or using first/last and shift (ruby), Time: O(nlog(n)), Space: O(1)
