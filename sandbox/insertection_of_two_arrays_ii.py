class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        nums1, nums2 = sorted(nums1), sorted(nums2)
        result = []

        while nums1 and nums2:
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
