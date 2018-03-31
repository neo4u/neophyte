# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def three_sum_closest(nums, target)
  nums.sort!
	result, n = nums[0,3].reduce(:+), nums.length - 1

  0.upto(n) do |i|
    l, r = i + 1, n
    while l < r
      s = nums[i] + nums[l] + nums[r]
      result = s if (target - s).abs <  (target - result).abs
      if s < target
        l += 1
      elsif s > target
        r -= 1
      else
        return result
      end
    end
  end

  result
end