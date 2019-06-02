# @param {Integer[]} nums
# @return {Boolean}
def can_jump(nums)
    n = nums.size
    last_good = n - 1

    (n - 2).downto(0) do |i|
        last_good = i if i + nums[i] >= last_good
    end

    last_good == 0
end
