# @param {Integer[]} nums
# @return {Integer}
def find_peak_element(nums)
    n = nums.size
    l, r = 0, n - 1

    while l < r
        mid = (l + r) / 2
        nums[mid] < nums[mid + 1] ? l = mid + 1 : r = mid
    end

    l
end

# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/
