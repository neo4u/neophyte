# Approach 1: HashMap
def majority_element(nums)
    map = {}
    nums.each do |n| map[n] = map.fetch(n, 0) + 1 end

    map.max_by { |k, v| v }[0]
end

# Approach 2: Sort
def majority_element(nums)
    nums.sort[n / 2]
end

# 169. Majority Element
# https://leetcode.com/problems/majority-element/description/

# Approach 1: Hash map
# Approach 2: Sort
