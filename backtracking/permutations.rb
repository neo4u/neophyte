# @param {Integer[]} nums
# @return {Integer[][]}
def permute(nums)
    return [] if !nums || nums.empty?
    bt(nums)
end

def bt(nums, path = [], result = [])
    if nums.empty?
        result.push(path)
        return
    end

    0.upto(nums.size - 1) do |i|
        curr_removed = nums[0...i] + nums[i + 1...nums.size]
        bt(curr_removed, path + [nums[i]], result)
    end

    result
end

def permute(nums)
    return [] if !nums || nums.empty?
    bt(nums, nums.size)
end

def bt(nums, n, first = 0, results = [])
    if first == n - 1
        results.push(nums.dup)
        return results
    end 

    first.upto(n - 1) do |i|
        nums[first], nums[i] = nums[i], nums[first] if first != i
        bt(nums, n, first + 1, results)
        nums[first], nums[i] = nums[i], nums[first] if first != i
    end

    results
end

def permute(nums)
    return [] if !nums || nums.empty?
    @results = []
    bt(nums, nums.size)
    @results
end

def bt(nums, n, first = 0)
    return @results.push(nums.dup) if first == n - 1

    first.upto(n - 1) do |i|
        nums[first], nums[i] = nums[i], nums[first] if first != i
        bt(nums, n, first + 1)
        nums[first], nums[i] = nums[i], nums[first] if first != i
    end
end



# 46. Permutations
# https://leetcode.com/problems/permutations/description/

# bt(0, [1 2 3])
#     bt(1, [1,2,3])
#         bt(2, [1,2,3])
#            bt(3, [1,2,3]) results = [[1,2,3]]
#            ret
#         bt(2, [1,3,2])
#             bt(3, [1,3,2]) results = [[1,2,3], [1,3,2]]
#             ret
#     bt(1, [2,1,3])
#         bt(2, [2,1,3])
#             bt(3, [2,1,3]) results = [[1,2,3], [1,3,2], [2,1,3]]
#             ret
#         bt(2, [2,3,1])
#             bt(3, [2,3,1]) results = [[1,2,3], [1,3,2], [2,1,3], [2,3,1]]
#             ret
#     bt(1, [3,2,1])
#         bt(2, [3,2,1])
#             bt(3, [3,2,1]) results = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1]]
#             ret
#         bt(2, [3,1,2])
#             bt(3, [3,1,2]) results = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]
#             ret

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(permute([1,2,3]), [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,2,1],
    [3,1,2]
])
assert_equal(permute([1,2]), [[1, 2], [2, 1]])


# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]