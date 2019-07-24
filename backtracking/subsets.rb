def subsets(nums)
    return [] if !nums || nums.empty?
    bt(nums, 0)
end

def bt(nums, index, path = [], result = [])
    result.push(path)
    return if index == nums.size

    index.upto(nums.size - 1) do |i|
        bt(nums, i + 1, path + [nums[i]], result)
    end

    result
end


# [1,2,3]
# bt(0,[])
#     bt(1, [1])
#         bt(2,[1,2])
#             bt(3, [1,2,3])
#             return
#         return
#         bt(3,[1,3])
#         return
#     bt(2,[2])
#         bt(3,[2,3])
#         return
#     return
#     bt(3,[3])
#     return

#   { [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3] }

