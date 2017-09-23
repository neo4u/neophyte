class Array
  def radix_sort(base = 10)
    exp = 0
    a = dup
    max_num = a.max
    until max_num.zero?
      exp += 1
      max_num /= 10
    end

    exp.times do |i|
      base_i = base**i
      buckets = Array.new(2 * base) { [] }
      a.each do |num|
        digit = (num / base_i) % base
        digit += base if num >= 0
        buckets[digit] << num
      end
      a = buckets.flatten
    end
    a
  end
end

# p [1, 3, 8, 9, 0, 0, 8, 7, 1, 6].radix_sort
# p [170, 45, 75, 90, 2, 24, 802, 66].radix_sort
# p [170, 45, 75, 90, 2, 24, -802, -66].radix_sort
# p [100000, -10000, 400, 23, 10000].radix_sort