WITHIN_20 = %w[One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen].unshift("")
TENS = %w[Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety].unshift("")

# @param {Integer} num
# @return {String}
def number_to_words(num)
    return "Zero" if num == 0
    helper(num)
end

def helper(num)
    (if num < 20 then WITHIN_20[num]
    elsif num < 100 then TENS[num / 10] + " " + WITHIN_20[num % 10]
    elsif num < 1_000 then WITHIN_20[num / 100] + " Hundred " + helper(num % 100)
    elsif num < 1_000_000 then helper(num / 1000) + " Thousand " + helper(num % 1000)
    elsif num < 1_000_000_000 then helper(num / 1_000_000) + " Million " + helper(num % 1_000_000)
    else helper(num / 1_000_000_000) + " Billion " + helper(num % 1_000_000_000) end).strip
end


# Time: O(1), Depth of recursion is max of 6 [billion, million, thousand, hundred, tens, one]
# Space: O(1), Fix depth of recursion

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(number_to_words(12345), "Twelve Thousand Three Hundred Forty Five")
assert_equal(number_to_words(999_999), "Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine")
assert_equal(number_to_words(1), 'One')
assert_equal(number_to_words(0), 'Zero')
assert_equal(number_to_words(20), 'Twenty')
assert_equal(number_to_words(25), 'Twenty Five')
assert_equal(number_to_words(99), 'Ninety Nine')
assert_equal(number_to_words(100), 'One Hundred')
assert_equal(number_to_words(123), 'One Hundred Twenty Three')
assert_equal(number_to_words(200), 'Two Hundred')
assert_equal(number_to_words(1000), 'One Thousand')
assert_equal(number_to_words(1234), 'One Thousand Two Hundred Thirty Four')
assert_equal(number_to_words(1996), 'One Thousand Nine Hundred Ninety Six')
assert_equal(number_to_words(2000), 'Two Thousand')
assert_equal(number_to_words(999_001), 'Nine Hundred Ninety Nine Thousand One')
assert_equal(number_to_words(99_000_001), 'Ninety Nine Million One')
assert_equal(number_to_words(1_000_000_000), 'One Billion')
assert_equal(number_to_words(989_000_000_001), 'Nine Hundred Eighty Nine Billion One')
assert_equal(number_to_words(50868), "Fifty Thousand Eight Hundred Sixty Eight")
