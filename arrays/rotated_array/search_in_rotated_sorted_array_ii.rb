def search(nums, target)
    l, r = 0, nums.size - 1

    while l <= r
        l += 1 while l < r && nums[l] == nums[l + 1]
        r -= 1 while l < r && nums[r] == nums[r - 1]
        mid = (l + r) / 2
        return true if nums[mid] == target

        if nums[mid] < nums[r]
            target.between?(nums[mid], nums[r]) ? l = mid + 1 : r = mid - 1
        else
            target.between?(nums[l], nums[mid]) ? r = mid - 1 : l = mid + 1
        end
    end

    false
end


# 81. Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

# Key Insights:
# 1. One of Left sub-array or right-subarray has to be sorted
# 2. We eliminate half using target and check the other half.

