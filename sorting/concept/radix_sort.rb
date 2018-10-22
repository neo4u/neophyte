# -------------------------------------------------------------------------------
# Adding an array method to do radix sort that handles negative numbers
# using a bucket size of  2 * base
# -------------------------------------------------------------------------------
class Array
  def radix_sort(base = 10)
    a = dup
    rounds = (Math.log(a.minmax.map(&:abs).max) / Math.log(base)).floor + 1

    rounds.times do |i|
      buckets = Array.new(2 * base) { [] }
      base_i = base**i
      a.each do |n|
        digit = (n / base_i) % base
        digit += base if 0 <= n
        buckets[digit] << n
      end
      a = buckets.flatten
    end
    a
  end

  def radix_sort!(base = 10)
    replace radix_sort(base)
  end
end

# p [1, 3, 8, 9, 0, 0, 8, 7, 1, 6].radix_sort
# p [170, 45, 75, 90, 2, 24, 802, 66].radix_sort
# p [170, 45, 75, 90, 2, 24, -802, -66].radix_sort
# p [100_000, -10_000_000, 400, 23, 1_000].radix_sort
