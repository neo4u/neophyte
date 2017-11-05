# @param {Integer[]} nums
# @return {Integer[][]}
def three_sum(nums)
  nums.sort!
  result = []
  0.upto(nums.size - 1) do |i|
    next if i > 0 && nums[i] == nums[i - 1]     # Skip duplicates
    l, r = i + 1, nums.size - 1
    while l < r
      s = nums[i] + nums[l] + nums[r]
      if s.zero?
        result.push([nums[i], nums[l], nums[r]])
        l += 1 while l < r && nums[l] == nums[l + 1] # Skip duplicates
        r -= 1 while l < r && nums[r] == nums[r - 1] # Skip duplicates
        l += 1
        r -= 1
      elsif s < 0
        l += 1
      elsif s > 0
        r -= 1
      end
    end
  end

  result
end

# Should be [[-1,-1,2],[-1,0,1]]
p three_sum([-1,0,1,2,-1,-4])