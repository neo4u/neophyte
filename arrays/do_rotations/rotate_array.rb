

# Approach 2: Using extra array
# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate_extra_array(nums, k)
    n = nums.size
    a = Array.new(n)
    k %= n

    0.upto(n - 1) do |i|
        # puts "from: #{i} | to: #{(i + k) % n}"
        a[(i + k) % n] = nums[i]
    end
    0.upto(n - 1) do |i| nums[i] = a[i] end
end

# Approach 3: Using cyclic replacements
# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate_loop(nums, k)
    n, k, j = nums.size, k % nums.size, 0
    size = nums.size

    while n > 0 && k % n != 0
        puts "before: #{nums} k: #{k} | n: #{n} | j: #{j} | k%n: #{k % n}"
        0.upto(k - 1) do |i|
            puts "  before: #{nums} k: #{k} | n: #{n} | j: #{j} | k%n: #{k % n}"
            nums[j + i], nums[size - k + i] = nums[size - k + i], nums[j + i]
            puts "  after: #{nums} k: #{k} | n: #{n} | j: #{j} | k%n: #{k % n}"
        end

        n, j = n - k, j + k
        k %= n
        puts "after: #{nums} k: #{k} | n: #{n} | j: #{j} | k%n: #{k % n}"
    end
end

def rotate_loop(nums, k)
    n, k, j = nums.size, k % nums.size, 0
    size = nums.size

    while n > 0 && k % n != 0
        puts "before: #{nums} k: #{k} | n: #{n} | j: #{j} | k%n: #{k % n}"
        0.upto(k - 1) do |i|
            puts "  before: #{nums} k: #{k} | n: #{n} | j: #{j} | k%n: #{k % n}"
            nums[j + i], nums[size - k + i] = nums[size - k + i], nums[j + i]
            puts "  after: #{nums} k: #{k} | n: #{n} | j: #{j} | k%n: #{k % n}"
        end

        n, j = n - k, j + k
        k %= n
        puts "after: #{nums} k: #{k} | n: #{n} | j: #{j} | k%n: #{k % n}"
    end
end


# Approach 4: Using reverse
def rotate(nums, k)
    n = nums.size
    k %= n

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
end

def reverse(nums, s, e)
    while s <= e
        nums[s], nums[e] = nums[e], nums[s]
        s += 1; e -= 1
    end
end

# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/description/

# All solutions in python
# https://leetcode.com/problems/rotate-array/discuss/54426/Summary-of-solutions-in-Python

# Approach 1: Brute-Force
# Time: O(k * n)
# Space: O(1)

# Approach 2: Using extra array
# Time: O(n)
# Space: O(n)

# Approach 3: Using cyclic replacements, Using group theory
# Steps:
# 1. We do swap within sets
# 2. Number of sets is given by the GCD
# 3. We have a while loop to loop through sets
# 4. We have an inner loop to loop within the set and swap elements
# 5. 
# Time: O(n)
# Space: O(1)

# Approach 4: Using reverse
# Steps:
# 1. Reverse entire array
# Before: [1, 2, 3, 4, 5, 6, 7]
# After:  [7, 6, 5, 4, 3, 2, 1]

# 2. Reverse first k elements
# Before: [7, 6, 5, 4, 3, 2, 1]
# After:  [5, 6, 7, 4, 3, 2, 1]

# 3. Reverse last n - k elements
# Before: [7, 6, 5, 4, 3, 2, 1]
# After:  [5, 6, 7, 1, 2, 3, 4]

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

arr1 = [1,2,3,4,5,6,7]
rotate_extra_array(arr1, 3)
assert_equal(arr1, [5,6,7,1,2,3,4])

arr2 = [1,2,3,4,5]
rotate_extra_array(arr2, 3)
assert_equal(arr2, [3,4,5,1,2])

arr3 = [-1,-100,3,99]
rotate_extra_array(arr3, 2)
assert_equal(arr3, [3,99,-1,-100])

# # Approach 3 tests: Using cyclic replacements
arr1 = [1,2,3,4,5,6,7]
rotate_cyclic(arr1, 3)
assert_equal(arr1, [5,6,7,1,2,3,4])

# arr2 = [1,2,3,4,5]
# rotate_cyclic(arr2, 3)
# assert_equal(arr2, [3,4,5,1,2])

# arr3 = [-1,-100,3,99]
# rotate_cyclic(arr3, 2)
# assert_equal(arr3, [3,99,-1,-100])

# Approach 4: Using reverse
arr1 = [1,2,3,4,5,6,7]
rotate(arr1, 3)
assert_equal(arr1, [5,6,7,1,2,3,4])

arr2 = [1,2,3,4,5]
rotate(arr2, 3)
assert_equal(arr2, [3,4,5,1,2])

arr3 = [-1,-100,3,99]
rotate(arr3, 2)
assert_equal(arr3, [3,99,-1,-100])
