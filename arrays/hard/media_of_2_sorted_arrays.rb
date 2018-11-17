# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(nums1, nums2)
    m, n = nums1.size, nums2.size

    # to ensure m<=n
    nums1, nums2, m, n = nums2, nums1, n, m if m > n
    imin, imax, halflen = 0, m, (m + n + 1) / 2

    while imin <= imax
        i = (imin + imax) / 2
        j = halflen - i
  
        if i < imax && nums2[j - 1] > nums1[i] # i is too small
            imin = i + 1
        elsif i > imin && nums1[i - 1] > nums2[j] # i is too big
            imax = i - 1
        else # i is perfect
            max_left = 0
            if i == 0 then max_left = nums2[j - 1]
            elsif j == 0 then max_left = nums1[i - 1]
            else max_left = [nums1[i - 1], nums2[j - 1]].max end
    
            return max_left if (m + n).odd?
    
            min_right = 0
            if i == m then min_right = nums2[j]
            elsif j == n then min_right = nums1[i]
            else min_right = [nums2[j], nums1[i]].min end
    
            return (max_left + min_right) / 2.0
        end
    end

    0.0
end

# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# 4. Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

require 'test/unit'
extend Test::Unit::Assertions

nums1 = [1, 3]
nums2 = [2]
assert_equal(find_median_sorted_arrays(nums1, nums2), 2.0)
nums1 = [1, 2]
nums2 = [3, 4]
assert_equal(find_median_sorted_arrays(nums1, nums2), 2.5)
