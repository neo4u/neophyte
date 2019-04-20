# Approach 1: Regex and Stack
# def calculate(s)
#     res, op, stack = 0, nil, []

# end

# Approach 2: 1 Stack
# @param {String} s
# @return {Integer}
def calculate(s)
    res, n, sign, stack = 0, 0, 1, []

    s.each_char do |c|
        if c.between?('0', '9')
            n = n*10 + c.to_i
        elsif '-+'.include?(c)
            res += sign * n
            sign = c == "+" ? 1 : -1
            n = 0
        elsif c == '('
            stack.push(res)
            stack.push(sign)
            res, sign = 0, 1
        elsif c == ')'
            res += sign * n
            res *= stack.pop() # give the result inside the parentheses the appropriate sign from the stack
            res += stack.pop() # Add the result of parantheses with the op before it
            n = 0
        end
    end

    res + n*sign
end

# Approach 3: 2 Stacks
# Refer to java file with same name

# 224. Basic Calculator
# https://leetcode.com/problems/basic-calculator/description/

# Example: (1+(4+5+2)-3)+(6+8) Answer = 23
# c: (
# before: num: 0 | sign: 1 | stack: [] | res: 0
# after: num: 0 | sign: 1 | stack: [0, 1] | res: 0
# c: 1
# before: num: 0 | sign: 1 | stack: [0, 1] | res: 0
# after: num: 1 | sign: 1 | stack: [0, 1] | res: 0
# c: +
# before: num: 1 | sign: 1 | stack: [0, 1] | res: 0
# after: num: 0 | sign: 1 | stack: [0, 1] | res: 1
# c: (
# before: num: 0 | sign: 1 | stack: [0, 1] | res: 1
# after: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 0
# c: 4
# before: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 0
# after: num: 4 | sign: 1 | stack: [0, 1, 1, 1] | res: 0
# c: +
# before: num: 4 | sign: 1 | stack: [0, 1, 1, 1] | res: 0
# after: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 4
# c: 5
# before: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 4
# after: num: 5 | sign: 1 | stack: [0, 1, 1, 1] | res: 4
# c: +
# before: num: 5 | sign: 1 | stack: [0, 1, 1, 1] | res: 4
# after: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 9
# c: 2
# before: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 9
# after: num: 2 | sign: 1 | stack: [0, 1, 1, 1] | res: 9
# c: )
# before: num: 2 | sign: 1 | stack: [0, 1, 1, 1] | res: 9
# after: num: 0 | sign: 1 | stack: [0, 1] | res: 12
# c: -
# before: num: 0 | sign: 1 | stack: [0, 1] | res: 12
# after: num: 0 | sign: -1 | stack: [0, 1] | res: 12
# c: 3
# before: num: 0 | sign: -1 | stack: [0, 1] | res: 12
# after: num: 3 | sign: -1 | stack: [0, 1] | res: 12
# c: )
# before: num: 3 | sign: -1 | stack: [0, 1] | res: 12
# after: num: 0 | sign: -1 | stack: [] | res: 9
# c: +
# before: num: 0 | sign: -1 | stack: [] | res: 9
# after: num: 0 | sign: 1 | stack: [] | res: 9
# c: (
# before: num: 0 | sign: 1 | stack: [] | res: 9
# after: num: 0 | sign: 1 | stack: [9, 1] | res: 0
# c: 6
# before: num: 0 | sign: 1 | stack: [9, 1] | res: 0
# after: num: 6 | sign: 1 | stack: [9, 1] | res: 0
# c: +
# before: num: 6 | sign: 1 | stack: [9, 1] | res: 0
# after: num: 0 | sign: 1 | stack: [9, 1] | res: 6
# c: 8
# before: num: 0 | sign: 1 | stack: [9, 1] | res: 6
# after: num: 8 | sign: 1 | stack: [9, 1] | res: 6
# c: )
# before: num: 8 | sign: 1 | stack: [9, 1] | res: 6
# after: num: 0 | sign: 1 | stack: [] | res: 23

# Time: O(n)
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(calculate("1 + 1"), 2)
assert_equal(calculate(" 2-1 + 2 "), 3)
assert_equal(calculate("(1+(4+5+2)-3)+(6+8)"), 23)
