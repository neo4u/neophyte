# @param {Integer[]} numbers
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)
    l, r = 0, numbers.size - 1
    
    while l < r
        sum = numbers[l] + numbers[r]
        if sum == target
            return [l + 1, r + 1]
        elsif sum < target
            l += 1
        elsif sum > target
            r -= 1
        end
    end

    nil
end