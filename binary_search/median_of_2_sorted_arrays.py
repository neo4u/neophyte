from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m == n: return self.find_median_sorted_arrays_same_size(nums1, nums2)

        # We ensure that n >= m so that j is always >= 0
        if n < m: nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, halflen = 0, m, (m + n + 1) // 2
        # The reason for halflen index = m + n + 1 is to play well with odd and even total len
        # Ex: m = 4, n = 4, halflen = 4, m = 4, n = 5, halflen = 4, 4 in both cases
        # Ex: m = 2, n = 3, halflen = 3, m = 3, n = 3, halflen = 3, 3 in both cases

        while imin <= imax:
            i = (imin + imax) // 2
            j = halflen - i

            if i < imax and nums2[j - 1] > nums1[i]:    imin = i + 1    # i is too small
            elif i > imin and nums1[i - 1] > nums2[j]:  imax = i - 1    # i is too big
            else:                                                       # i is perfect
                max_left = 0
                if i == 0:      max_left = nums2[j - 1]
                elif j == 0:    max_left = nums1[i - 1]
                else:           max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1: return max_left

                min_right = 0
                if i == m:      min_right = nums2[j]
                elif j == n:    min_right = nums1[i]
                else:           min_right = min(nums2[j], nums1[i])

                return (max_left + min_right) / 2

    def find_median_sorted_arrays_same_size(self, nums1, nums2):
        n = len(nums1)
        mid = n // 2
        if n <= 0: return -1
        if n == 1: return (nums1[0] + nums2[0]) / 2
        if n == 2: return (max(nums1[0], nums2[0]) + min(nums1[1], nums2[1])) / 2

        m1, m2 = self.median_sorted(nums1), self.median_sorted(nums2)
        if m1 == m2: return m1

        # if m1 < m2 then median must exist in ar1[m1....] and ar2[....m2]
        if m1 < m2:
            if n % 2 == 0:  return self.find_median_sorted_arrays_same_size(nums1[mid - 1:], nums2[:mid + 1])
            else:           return self.find_median_sorted_arrays_same_size(nums1[mid:], nums2[:mid + 1])
        else:
            if n % 2 == 0:  return self.find_median_sorted_arrays_same_size(nums2[mid - 1:], nums1[:mid + 1])
            else:           return self.find_median_sorted_arrays_same_size(nums2[mid:], nums1[:mid + 1])

    def median_sorted(self, a):
        n = len(a)
        mid = n // 2
        if n % 2 == 0:  return (a[mid] + a[mid - 1]) / 2
        else:           return a[n // 2]



# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# Important points
# 1. We do a binary search of nums1 to find index i
#    and use i to calc j in nums2
# 2. i moves the opposite direction of j
# 3. imin and imax set the bounds of the iteration of the while loop
# 4. when increasing imax we need to ensure i > imin cuz imax is set relative to i
# 5. Similarly when decreasing imin, we need to ensure i < imax as imin is set relative to i and we want to ensure i 

# Finally, we need to partition both arrays using the i and j such that we get two halves
# that we get by combining left part of nums1 and nums2 and right part of nums1 and nums2
# NOTE: If (m + n) is odd, then left part will have 1 element extra, and max_left is the median
#       if (m + n) is even, then left and right parts are equal len, and median is (max_left + min_right) / 2.0
# For the above conditions to work, we should have m <= n, so if m > n, we swap nums1 and nums2

# We want to find a condition that:
# 1. All the elements in left half (combo of both left parts) are < all elements of right part
# 2. We're within the imax and imin bounds

# Time Complexity:  O(log(min(m, n)))
#                   O(log(n)) for same size
# Space Complexity: O(1)

sol = Solution()
assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
assert sol.findMedianSortedArrays([1, 2], [2]) == 2.0

assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert sol.findMedianSortedArrays([2, 3], [4, 5]) == 3.5
assert sol.findMedianSortedArrays([1, 2, 3], [4, 5, 6]) == 3.5
