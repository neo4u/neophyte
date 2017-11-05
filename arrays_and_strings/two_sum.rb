# Brute-Force
# def two_sum(nums, target)
#   0.upto(nums.size - 1) do |i|
#     (i + 1).upto(nums.size - 1) do |j|
#       return [i, j] if nums[i] + nums[j] == target
#     end
#   end
# end

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  d = {}
  nums.each_with_index do |n, i|
    m = target - n
    return [d[m], i] if d.key?(m)
    d[n] = i
  end
  nil
end


nums = [3, 3]
target = 6
p two_sum(nums, target)

nums = [3,2,4]
target = 6
p two_sum(nums, target)

nums = [3, 3, 5]
target = 0
p two_sum(nums, target)