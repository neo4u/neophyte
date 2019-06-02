# @param {Integer[]} nums
# @return {Integer[][]}
def permute_unique(nums)
    return [] if !nums || nums.empty?
    nums.sort!()
    bt(nums)
end

def bt(nums, path = [], result = [])
    if nums.empty?
        result.push(path)
        return
    end

    0.upto(nums.size - 1) do |i|
        next if i > 0 && nums[i] == nums[i - 1] # Skip duplicates, after i crosses 0
        nums_with_curr_removed = nums[0...i] + nums[i + 1...nums.size]
        bt(nums_with_curr_removed, path + [nums[i]], result)
    end

    result
end


# # @param {Integer[]} nums
# # @return {Integer[][]}
# def permute_unique(nums)
#     nums.sort!
#     bt(nums, nums.size)
# end

# def bt(nums, n, first = 0, result = [])
#     result.push(nums.dup) if first == n - 1

#     first.upto(n - 1) do |i|
#         next if i > first && nums[i] == nums[first]
#         swap(nums, first, i) if first != i
#         bt(nums, n, first + 1, result)
#         swap(nums, i, first) if first != i
#     end

#     result
# end

# def swap(nums, i, j)
#     nums[i], nums[j] = nums[j], nums[i]
# end



def permute_unique(nums)
    @result = []
    bt(nums, nums.size)
    @result
end

def bt(nums, n, first = 0)
    @result.push(nums.dup) if first == n - 1
    used = Set.new()
    first.upto(n - 1) do |i|
        next if used.include?(nums[i])
        used.add(nums[i])
        swap(nums, first, i) if first != i
        bt(nums, n, first + 1)
        swap(nums, first, i) if first != i
    end
end

def swap(nums, i, j)
    nums[i], nums[j] = nums[j], nums[i]
end





# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(permute_unique([1,1,2]), [
    [1,1,2],
    [1,2,1],
    [2,1,1]
])
assert_equal(permute_unique([1,2,2,4]), [
    [1,2,2,4],
    [1,2,4,2],
    [1,4,2,2],
    [2,1,2,4],
    [2,1,4,2],
    [2,2,1,4],
    [2,2,4,1],
    [2,4,1,2],
    [2,4,2,1],
    [4,1,2,2],
    [4,2,1,2],
    [4,2,2,1]
])

