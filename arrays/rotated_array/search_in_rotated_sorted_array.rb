def search(nums, target)
    l, r = 0, nums.size - 1

    while l <= r
        mid = (l + r) / 2
        return mid if nums[mid] == target

        if nums[mid] < nums[r]
            target.between?(nums[mid], nums[r]) ? l = mid + 1 : r = mid - 1
        else
            target.between?(nums[l], nums[mid]) ? r = mid - 1 : l = mid + 1
        end
    end

    -1
end


# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/


# Key Insights:
# 1. One of Left sub-array or right-subarray has to be sorted
# 2. We eliminate half using target and check the other half.

