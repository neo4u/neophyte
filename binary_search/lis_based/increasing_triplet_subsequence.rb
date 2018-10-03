# @param {Integer[]} nums
# @return {Boolean}
def increasing_triplet(nums)
    tails = Array.new(3)

    nums.each do |x|
        pos = binary_search(tails, x)
        tails[pos] = x
        size = [pos + 1, size].max
        return true if size == 3
    end
    false
end

def binary_search(a, x)
    l, r = 0, a.size
    while l < r
        mid = (l + r) / 2
        tails[mid] < x ? l = mid + 1 : r = mid
    end
    l
end

# @param {Integer[]} nums
# @return {Boolean}
def increasing_triplet_alternative(nums)
    i, j = Float::INFINITY, Float::INFINITY
    
    nums.each do |x|
       if x <= i
           i = x
       elsif x <= j
           j = x
       else
           return true
       end
    end

    false
end

# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/

# Today, I revisited this problem. This time,
# I don't think about how to solve it, instead I want to think about "how to think about it".
# Ok, so I read the description again, then I realize,
# it is asking about some sort of "increasing subsequence" with size 3.
# Then I think about all the relevant algorithm I know,
# for example, the famous "Longest Increasing Subsequence" (LIS) problem.
# Then I instantly got a solution: Find the LIS of the input, and if it is greater than 3, return true;
# Looks like a working solution, what's its complexity then:

# There is a O(nlogk) solution to LIS
# (if you don't know it, just search this problem in Leetcode and see the discussions),
# where n is the array length and k is the length of LIS. Here, k is no larger than 2
# so it is O(nlog2) = O(n). Very well, a O(n) solution is so easily obtained here: