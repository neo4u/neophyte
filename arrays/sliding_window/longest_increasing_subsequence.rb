# Approach 2: Binary Search
# @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)
    tails, size = Array.new(nums.size), 0
    nums.each do |x|
        # Binary search on tails to find the right postion for x
        pos = bin_search(tails, x, size)

        # At this point the result of the binary search is in pos
        tails[pos] = x # if tails[i-1] < x <= tails[i], update tails[i]
        size = [pos + 1, size].max # pos + 1 is to convert from index to length
    end
    size
end

def bin_search(a, x, size)
    l, r = 0, size
    while l < r
        mid = (l + r) / 2
        a[mid] < x ? l = mid + 1 : r = mid
    end
    l
end


# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

# Approach 1: Brute-Force Time: O(2^n), Space: O(n^2)
# Approach 2: Recursion with memoization, Time: O(n^2), Space: O(n^2)
# Approach 3: DP, Time: O(n^2), Space: O(n)
# Approach 4: DP with binary search, Time: O(nlog(n)), Space: O(1)

# Intuition and Algorithm
# This solution is essentialy binary search + Dynamic Programming (tails)
# tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i] scanned so far.
# For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

# len = 1:  [4], [5], [6], [3] => tails[0] = 3
# len = 2:  [4, 5], [5, 6]     => tails[1] = 5
# len = 3:  [4, 5, 6]          => tails[2] = 6

# We can easily prove that tails is a increasing array.
# Therefore it is possible to do a binary search in tails array to find the one needs update.
# Each time we only do one of the two:
# (1) if x is larger than all tails, append it, increase the size by 1
# (2) if tails[i-1] < x <= tails[i], update tails[i]
# The above replace or append is enforce by the pos returned by the binary search
# Appending means length of LIS has increased by 1
# Replacing means we found a better tail for the curr LIS

