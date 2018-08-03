# @param {String} s
# @return {String}
def reverse_string(s)
  return s if s.empty?
  0.upto(s.size/2 - 1) do |i|
    s[i], s[-i -1] = s[-i - 1], s[i]
  end

  s
end


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(reverse_string('a.'), '.a')
assert_equal(reverse_string('hello'), 'olleh')
assert_equal(reverse_string("a ba"), "ab a")
assert_equal(reverse_string("abcd"), "dcba")