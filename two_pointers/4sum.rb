# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[][]}
def four_sum(nums, target)
  n = nums.length
  nums.sort!
  res = []

  (0..n - 4).each do |a|                              	 # Iterate from 0 to 3rd from last
    next if a > 0 && nums[a - 1] == nums[a]              # Skip Duplicates
    (a + 1..n - 3).each do |b|                        	 # Iterate from 1 after to 1 before last ??? Why
      next if b > a + 1 && nums[b - 1] == nums[b]        # Skip Duplicate
      c = b + 1
      d = n - 1
      while c < d
        s = nums[a] + nums[b] + nums[c] + nums[d]
        if s == target
          res.push([nums[a], nums[b], nums[c], nums[d]])
          while c < d && nums[c += 1] == nums[c - 1] do end
          while c < d && nums[d -= 1] == nums[d + 1] do end
        elsif s < target
          c += 1
        else
          d -= 1
        end
      end
    end
  end

  res
end

res = four_sum([-2, -1, 2, 5, 5, 7, 8], 12)
p res