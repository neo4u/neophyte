# @param {String} num1
# @param {String} num2
# @return {String}
def multiply(num1, num2)
    product, fraction = 0, 0

    num1.each_char do |digit1|
        product *= 10
        fraction = 0

        num2.each_char do |digit2|
            fraction *= 10
            fraction += digit1.to_i * digit2.to_i
        end
        product += fraction
    end

    product.to_s
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(multiply("828", "2"), "1656")
assert_equal(multiply("2", "828"), "1656")
assert_equal(multiply("123", "1"), "123")
assert_equal(multiply("999", "999"), "998001")

# O(m * n)
# Iterate through the chars of first number
# Simple Demo for 25 x 34
# n1, n2 = 25, 34

# new d1 (2, 3)
# Before: product, fraction, d1, d2 = 0, 0, 2, 3
# new d2 (2, 4)
# After: fraction, product = 6, 6
# new d2 (2, 4)
# fraction = 60, product = 0
# product, fraction, d1, d2 = 0, 0, 2, 4 before
# product, fraction, d1, d2 = 0, 68
# End of inner loop: product, fraction = 68, 68

# new d1
# Before: product, fraction, d1, d2 = 68, 68, 5, 3
# product, fraction = 680, 0
# new d2 (5, 3)
# fraction = 0 * 10
# fraction = 0 + 5 * 3 = 15
# end of inner loop for 5,3
# new d2 (5, 4)
# product, fraction, d1, d2 = 68, 68, 5, 4
# fraction = 10 * 15
# fraction = 150 + 20  = 170
# end of new d1 (5, 4)
# product = 680 + 170 = 850


