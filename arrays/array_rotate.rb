# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate(nums, k)
  n, k, cnt, strt = nums.length, k % nums.length, 0, 0
  while cnt < n
    puts "while looping"
    cur = strt
    prv = nums[strt]
    begin
      puts "looping"
      puts "BEFORE: start: #{strt} | prev: #{prv} | curr: #{cur} | cnt: #{cnt}"
      p nums
      nxt = (cur + k) % n
      tmp = nums[nxt]
      nums[nxt] = prv
      prv = tmp
      cur  = nxt
      cnt += 1
      puts "AFTER: start: #{strt} | prev: #{prv} | curr: #{cur} | cnt: #{cnt}"
      break if strt == cur
    end
  end
  puts "\n"
  puts "\n"
  nums
end

# # @param {Integer[]} nums
# # @param {Integer} k
# # @return {Void} Do not return anything, modify nums in-place instead.
# def rotate(nums, k)
#   l = nums.length
#   k = k % l
#   return if k <= 0 || !k

# 	kl_gcd = l.gcd(k)

# 	repeats = (kl_gcd > 1) ? kl_gcd : 1
#   puts repeats
#   i = j = 0
#   while i < repeats do
#     j = i
#     temp_prev = nums[j]
#     temp_next = nil
#     begin 
#       next_j = (j + k) % l
#       temp_next = nums[next_j]
#       nums[next_j] = temp_prev
#       temp_prev = temp_next
#       j = next_j
#     end while j != i
#     i += 1
#   end

#   nums
# end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(rotate([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])
assert_equal(rotate([1,2,3,4,5], 3), [3,4,5,1,2])
