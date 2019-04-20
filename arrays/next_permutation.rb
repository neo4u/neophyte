# Condensed and for local testing
def next_permutation(nums)
    n = nums.size
    r = n - 1
    r -= 1 while nums[r - 1] >= nums[r]  && r > 0
    return reverse(nums, 0, n - 1) if r == 0

    pivot, scssr = r - 1, 0
    (n - 1).downto(pivot) do |i|
        next if nums[i] <= nums[pivot]
        scssr = i
        break
    end
    nums[scssr], nums[pivot] = nums[pivot], nums[scssr]
    reverse(nums, pivot + 1, n - 1)
end

def reverse(nums, l, r)
    while l < r
        nums[l], nums[r] = nums[r], nums[l]
        l += 1; r -= 1
    end

    nums
end


# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def next_permutation2(nums)
    n = nums.size
    r = n - 1

    # Select the right most element that breaks the property of a[i - 1] >= a[i],
    # which is the 1st valley from back
    r -= 1 while nums[r] <= nums[r - 1] && r - 1 >= 0
    return reverse2(nums, 0, n - 1) if r == 0 # Case for whole array in dec order like: ['3', '2', '1']

    # find pivot and successor are the candidates for the swap
    pivot, successor = r - 1, 0

    # Find the next immediate larger element to pivot element
    (n - 1).downto(pivot) do |i|
        next if nums[i] <= nums[pivot]
        successor = i
        break
    end

    # swap pivot and successor
    nums[pivot], nums[successor] = nums[successor], nums[pivot]

    # reverse suffix
    reverse2(nums, pivot + 1, n - 1)
end

def reverse2(nums, l, r)
    while l < r
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    end
end

# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

# Approach 1: Brute force, Time: O(n!), Space: O(n)
# Approach 2: Single pass approach, Time: O(n), Space: O(1)

# Steps:
# 1. Scan from right with a loop invariant that all elements to the right of current are sorted in decreasing order
# 2. We try to find the consequtive elements such that the property of a[i] <= a[i - 1] is broken i.e. a[i - 1] < a[i]
# 3. We find the element to the right of a[i - 1] that is just larger than a[i - 1] and swap a[i - 1], a[j]
# 4. We sort in dec order to the right of a[i - 1]/pivot to get the next lexicographical perm.
# 5. For decreasing order this happens to be the entire array.

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(next_permutation([1,2,3]), [1,3,2])
assert_equal(next_permutation([3,2,1]), [1,2,3])
assert_equal(next_permutation([1,1,5]), [1,5,1])
