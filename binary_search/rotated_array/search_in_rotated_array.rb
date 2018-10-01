# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
    l, r = 0, nums.size - 1
  
    while l <= r
        mid = (l + r) / 2
        return mid if nums[mid] == target
      
        if nums[l] <= nums[mid]
            target.between?(nums[l], nums[mid]) ? r = mid - 1 : l = mid + 1
        else
            target.between?(nums[mid], nums[r]) ? l = mid + 1 : r = mid - 1
        end
    end

    -1
end
