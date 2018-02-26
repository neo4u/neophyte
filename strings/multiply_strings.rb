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
