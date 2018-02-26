# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
  nums.each { |num| nums << nums.delete_at(nums.find_index(num)) if num.zero? }
end

# Solution
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
  count = nums.count(0)
  nums.delete(0)
  count.times do
    nums << 0
  end
  nums
end

nums = [0,1,0,3,12]
move_zeroes(nums)
p nums

nums = [0,0,1]
move_zeroes(nums)
p nums