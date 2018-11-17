# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    hash = Hash.new(0)
    nums.each do |num|
        return true if hash.key?(num)
        hash[num] += 1
    end

    false
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(contains_duplicate([1,2,3,1]), true)
assert_equal(contains_duplicate([1,2,3,4]), false)
assert_equal(contains_duplicate([1,1,1,3,3,4,3,2,4,2]), true)
