# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(nums1, nums2)
    m, n = nums1.size, nums2.size

    # We ensure that n >= m so that j is always >= 0
    nums1, nums2, m, n = nums2, nums1, n, m if m > n
    imin, imax, halflen = 0, m, (m + n + 1) / 2
    # The reason for halflen index = m + n + 1 is to play well with odd and even total len
    # Ex: m = 4, n = 4, halflen = 4, m = 4, n = 5, halflen = 4, 4 in both cases
    # Ex: m = 2, n = 3, halflen = 3, m = 3, n = 3, halflen = 3, 3 in both cases

    while imin <= imax
        i = (imin + imax) / 2
        j = halflen - i
  
        if i < imax && nums2[j - 1] > nums1[i]      # i is too small
            imin = i + 1
        elsif i > imin && nums1[i - 1] > nums2[j]   # i is too big
            imax = i - 1
        else                                        # i is perfect
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
end

def find_median_sorted_arrays_same_size(nums1, nums2)
    n = nums1.size
    mid = n / 2
    return -1 if n <= 0
    return (nums1[0] + nums2[0]) / 2.0 if n == 1
    return ([nums1[0], nums2[0]].max + [nums1[1], nums2[1]].min) / 2.0 if n == 2

    m1, m2 = median_sorted(nums1), median_sorted(nums2)
    return m1 if m1 == m2

    # if m1 < m2 then median must exist in ar1[m1....] and ar2[....m2]
    if m1 < m2
        if n.even?
            find_median_sorted_arrays_same_size(nums1[mid - 1...n], nums2[0...mid + 1])
        else
            find_median_sorted_arrays_same_size(nums1[mid...n], nums2[0...mid + 1])
        end
    else
        if n.even?
            find_median_sorted_arrays_same_size(nums2[mid - 1...n], nums1[0...mid + 1])
        else
            find_median_sorted_arrays_same_size(nums2[mid...n], nums1[0...mid + 1])
        end
    end
end

def median_sorted(a)
    n = a.size
    mid = n / 2
    if n.even?
        (a[mid] + a[mid - 1]) / 2.0
    else
        a[n / 2]
    end
end

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

require 'test/unit'
extend Test::Unit::Assertions

nums1 = [1, 3]
nums2 = [2]
assert_equal(find_median_sorted_arrays(nums1, nums2), 2.0)
nums1 = [1, 2]
nums2 = [3, 4]
assert_equal(find_median_sorted_arrays(nums1, nums2), 2.5)


nums1 = [1, 2]
nums2 = [3, 4]
assert_equal(find_median_sorted_arrays_same_size(nums1, nums2), 2.5)

nums1 = [2, 3]
nums2 = [4, 5]
assert_equal(find_median_sorted_arrays_same_size(nums1, nums2), 3.5)

nums1 = [1,2,3]
nums2 = [4,5,6]
assert_equal(find_median_sorted_arrays_same_size(nums1, nums2), 3.5)