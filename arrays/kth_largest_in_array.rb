# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_kth_largest(nums, k)
    return if !nums || nums.empty?
    n = nums.size
    quick_select(nums, 0, n - 1, n - k) # Kth largest is at n - 1 - (k - 1) = (n - k)th index
end

def quick_select(a, l, r, k)            # Note the k here refers to (n - k) from the question stand-point
    return a[l] if l == r               # Base case of recursion
    mid = rand_partition(a, l, r)         # Pick the pivot using random partition

    if k < mid
        quick_select(a, l, mid - 1, k)    # kth smallest is in the lower partition
    elsif k > mid
        quick_select(a, mid + 1, r, k)    # kth smallest is in the higher partition
    else
        a[mid]                            # if mid == k return Pivot as the kth smallest
    end
end

def rand_partition(a, l, r)
    i = rand(l..r)                      # Pick a random index between l and r - 1 inclusive
    a[i], a[r] = a[r], a[i]             # Swap the last element with the one at i

    partition(a, l, r)                  # Return result of partition()
end

def partition(a, l, r)
    i = l - 1                           # Choose the index before the pth index
    pivot = a[r]                        # Choose the last element as pivot

    l.upto(r - 1) do |j|                # Loop from p to r-1 moving elements to either side of pivot
      next if a[j] > pivot              # Move to next element if element is already > than pivot element
      i += 1                            # Increment index i for current pivot placement index
      a[i], a[j] = a[j], a[i]           # Swap elements at pivot placement index with the current index j
    end

    a[i + 1], a[r] = a[r], a[i + 1]     # Move the pivot to its final place: index before which all elements < pivot
    i + 1                               # return pivot index
end

# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Key points:
# 1. We need Kth largest, not kth smallest for which is a known Algorithm
# 2. Array is unsorted
 
# Approach 1: Sort and select (n - k)th element, Time: O(n) Space: O(1) using in-place sort
# Approach 2: PriorityQueue, Time: O(nlog(k)) Space: O(k)
# Approach 3: Quick select for (n + 1 - k)th smallest without randomized partition,
#             Time: Avg. O(n), Worst. O(n^2), Space: O(1) 
# Approach 4: Quick select with randomized partition, Time: O(n), Space: O(1) [gauranteed by Blum-Floyd-Pratt-Rivest-Tarjan]

# Algorithm
# 1. Make Kth largest to (n - k)th smallest
# 2. For (n - k)th smallest call partition
# 3. Partition find a pivot index and swap elements around the pivot and returns the index,
#    such that all elements left of pivot are < pivot and to right are > pivot
# 4. if k is smaller than pivot index do a quickselect of first half
# 5. else if k > pivot index do a quick select of 2nd half

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_kth_largest([3,2,1,5,6,4], 2), 5)
assert_equal(find_kth_largest([3,2,3,1,2,4,5,5,6], 4), 4)
assert_equal(find_kth_largest([3,2], 4), 2)
assert_equal(find_kth_largest([], 5), nil)