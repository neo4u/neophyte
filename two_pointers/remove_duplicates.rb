# Less lines but not good for understanding
# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
    return 0 if !nums || nums.empty?
    i, j = 0, 0
    nums[i += 1] = nums[j] if nums[j] != nums[i] while (j += 1) < nums.size

    i + 1
end

# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
    return 0 if !nums || nums.empty?
    # i represents index upto which duplicates don't exist
    # j is a running pointer
    i, j = 0, 1

    while j < nums.length
        if nums[j] != nums[i]
            i += 1
            nums[i] = nums[j]
        end
        j += 1
    end

    i + 1 # convert index to size
end

# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# In place
# Since the array is already sorted, we can keep two pointers i and j,
# where i is the slow-runner while j is the fast-runner. As long as nums[i] = nums[j],
# we increment j to skip the duplicate.

# When we encounter nums[j] = nums[i],
# the duplicate run has ended so we must copy its value to nums[i + 1]nums[i+1].
# i is then incremented and we repeat the same process again until j reaches the end of array.