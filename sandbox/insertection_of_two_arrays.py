class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


import collections


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        result = set()

        num_set = set(nums2)
        for n in nums1:
            if n in num_set:
                result.add(n)

        return list(result)


import collections

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        nums1, nums2 = sorted(nums1), sorted(nums2)
        result = []

        while nums1 and nums2:
            while len(nums1) > 1 and nums1[0] == nums1[1]:
                nums1.pop(0)
            while len(nums2) > 1 and nums2[0] == nums2[1]:
                nums2.pop(0)
            top1, top2 = nums1[0], nums2[0]

            if top1 > top2:
                nums2.pop(0)
            elif top1 < top2:
                nums1.pop(0)
            else:
                result.append(top1)
                nums1.pop(0)
                nums2.pop(0)

        return result


# n2: [1,2,2,1]
# n1: [2,2]
