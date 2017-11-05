# @param {Integer} n
# @return {String}
def count_and_say(n)
  return '1' if n == 1
  nums = ['1']
  nums.push(process_num(nums.last)) until (n -= 1).zero?
  nums.last
end

def process_num(num)
  count, prev, str = 0, '', ''
  num.each_char do |c|
    if prev == c || prev == ''
      count += 1
    else
      str += count.to_s + prev
      count = 1
    end
    prev = c
  end
  str += count.to_s + prev
end

puts count_and_say(4)