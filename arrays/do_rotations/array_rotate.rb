# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate(nums, k)
    n, k, i, strt = nums.length, k % nums.length, 0, 0

    while i < n
        puts "while looping"
        cur = strt
        prv = nums[strt]
        loop do
            puts "looping"
            puts "BEFORE: start: #{strt} | prev: #{prv} | curr: #{cur} | cnt: #{i}"
            p nums
            nxt = (cur + k) % n
            tmp = nums[nxt]
            nums[nxt] = prv
            prv = tmp
            cur  = nxt
            i += 1
            puts "AFTER: start: #{strt} | prev: #{prv} | curr: #{cur} | cnt: #{i}"
            break if strt == cur
        end
    end

    puts "\n"
    puts "\n"
    nums
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(rotate([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])
assert_equal(rotate([1,2,3,4,5], 3), [3,4,5,1,2])
