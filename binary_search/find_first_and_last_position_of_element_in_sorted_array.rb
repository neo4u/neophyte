# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def search_range(nums, target)
    l = binary_search(nums, target, true)
    return [-1, -1] if l == nums.size || nums[l] != target
    r = binary_search(nums, target, false)
    [l, r - 1]
end

def binary_search(nums, target, left)
    l, r = 0, nums.size - 1

    while l <= r
        mid = (l + r) / 2
        target < nums[mid] || (left && nums[mid] == target) ? r = mid - 1 : l = mid + 1
    end

    l
end



def search_range(nums, target)
    l = binary_search_left(nums, target)
    return [-1, -1] if l == nums.size || nums[l] != target
    r = binary_search_right(nums, target)
    [l, r]
end

def binary_search_left(nums, target)
    l, r = 0, nums.size

    while l < r
        mid = (l + r) / 2
        target <= nums[mid] ? r = mid : l = mid + 1
    end

    l
end

def binary_search_right(nums, target)
    l, r = 0, nums.size

    while l < r
        mid = (l + r) / 2
        target < nums[mid] ? r = mid : l = mid + 1
    end

    l - 1
end



# 1,2,2,3,3,3,5,5,6,7,8
#             l
#           r

# 1,2,2,4,4,5,5,5,6,7,8
#               r
#               l
#               m
# Find right most with left = false (state at return of function, 6 is returned, so we take r - 1 == 5 as the answer for right)
# 1,2,2,3,3,3,5,5,6,7,8
#             l
#           r

# Find right most with left = true
# 1,2,2,4,4,5,5,5,6,7,8
# l       r

# 1,2,2,4,4,5,5,5,6,7,8
#         r
#       l

# 1,2,2,4,4,5,5,5,6,7,8
#       l r

# 1,2,2,4,4,5,5,5,6,7,8
#         r
#         l

# 1,2,2,4,4,5,5,5,6,7,8
#         r
#         l

# 1,2,2,4,4,5,5,5,6,7,8
#         r
#           l


# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


