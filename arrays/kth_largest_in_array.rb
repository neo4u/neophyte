# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_kth_largest(nums, k)
    n = nums.size
    quick_select(nums, 0, n - 1, n - k) # Kth largest is at n - 1 - (k - 1) = (n - k)th index
end

def quick_select(a, p, r, k)
    return a[p] if p == r                # Base case of recursion
    q = rand_partition(a, p, r)          # Pick the pivot using random partition

    if q > k
        quick_select(a, p, q - 1, k)    # kth smallest is in the lower partition
    elsif q < k
        quick_select(a, q + 1, r, k)    # kth smallest is in the higher partition
    else
        a[q]                            # if q == k return Pivot as the kth smallest
    end
end

def partition(a, p, r)
    i = p - 1                           # Choose the index before the pth index
    pivot = a[r]                        # Choose the last element as pivot

    (p...r).each do |j|                 # Loop from p to r-1 moving elements to either side of pivot
      next if a[j] > pivot              # Move to next element if array element greater than pivot
      i += 1                            # Increment index i for current placement index
      a[i], a[j] = a[j], a[i]           # Swap elements at pivot placement index with the current index j
    end
  
    a[i + 1], a[r] = a[r], a[i + 1]     # Move the pivot to its final place: index before which all elements < pivot
    i + 1                               # return pivot index
end

def rand_partition(a, p, r)
    i = rand(p..r)                      # Pick a random index between p and r
    a[i], a[r] = a[r], a[i]             # Swap the last element with the on at i

    partition(a, p, r)                  # Return result of partition()
end

# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Algorithm
# 1. Make Kth largest to kth smallest with the appropriate index. ( n + 1 - k for smallest)
# 2. For kth smallest call partition
# 3. Partition find a pivot index and swap elements around the pivot and returns the index
# 4. if k is smaller than pivot index do a quickselect of first half
# 5. else if k > pivot index do a quick select of 2nd half

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_kth_largest([3,2,1,5,6,4], 2), 5)
assert_equal(find_kth_largest([3,2,3,1,2,4,5,5,6], 4), 4)