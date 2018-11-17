# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
    i = 0 # Represents length of array without more than two duplicates
    nums.each do |n|
        if i < 2 || n != nums[i - 2]
            nums[i] = n
            i += 1
        end
    end

    i
end