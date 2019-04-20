# Write a function to expand string pattern to full string.
# Ex. 
# a -> a
# 2[a] -> aa
# 2[3[d]e] -> dddeddde

# Complete the 'expandPattern' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING pattern as parameter.

def expand_pattern(pattern, str = '')
    match_str_only = pattern.match(/(^\w+$)/)
    captures_str_only = match_str_only ? match_str_only.captures : []
    return captures_str_only[0] if !captures_str_only.empty?

    captures_group = pattern.match(/((\d+)\[(.*)\])(\w*)/).captures
    expand_pattern(captures_group[1]) * captures_group[0].to_i 
end

# https://www.hackerrank.com/work/tests/357011/questions

require 'test/unit'
extend Test::Unit::Assertions

# assert_equal(expand_pattern("a"), "a")
assert_equal(expand_pattern("2[a]"), "aa")
assert_equal(expand_pattern("3[d]e"), "ddde")
assert_equal(expand_pattern("2[3[d]e]"), "dddeddde")

