# Approach 1: Using two sets, Time: O(n), Space O(n)
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersection(nums1, nums2)
    set1, set2 = Set.new(nums1), Set.new()

    nums2.each do |n|
        set2.add(n) if set1.include?(n)
    end

    set2.to_a
end

# Approach 2: Using hash, Time: O(n), Space O(n)
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersect(nums1, nums2)
    map = Hash.new(0)
    result = []
    m, n = nums1.size, nums2.size
    nums1, nums2, m, n = nums2, nums1, n, m if m > n
    nums1.each { |num| map[num] += 1 }

    nums2.each do |num|
        next if map[num] == 0
        result.push(num)
        map[num] -= 1
    end
    
    result
end

# Approach 4. Like Two pointer approach using shift and first and last, first and last, Time: O(nlog(n)), Space: O(1)
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersection(nums1, nums2)
    nums1.sort!; nums2.sort!
    intersect = []

    while !nums1.empty? && !nums2.empty?
        if nums1.first < nums2.first
            nums1.shift
        elsif nums2.first < nums1.first
            nums2.shift
        else
            intersect << nums1.shift if intersect.last != nums1.first || intersect.empty?
            nums2.shift
        end
    end

    intersect
end

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
