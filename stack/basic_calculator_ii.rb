def calculate(s)
    s += '+0'
    stack, num, prev_op = [], 0, "+"

    s.each_char do |c|
        if c.between?('0', '9')
            num = num*10 + c.to_i
        elsif c != ' '
            if    prev_op == '-' then stack.push(-num)
            elsif prev_op == '+' then stack.push(num)
            elsif prev_op == '*' then stack.push(stack.pop * num)
            elsif prev_op == '/' then stack.push((stack.pop / num.to_f).to_i) end
            prev_op, num = c, 0
        end
    end

    stack.reduce(:+)
end


# Example: "3+2*2+0"
# i = 0, s[0] = 3, an operand, so we'll be setting num
# preOp = +, num = 3
# []

# i = 1, s[1] = +, an operator, so we'll be pushing to stack
# preOp = +, num = 3
# push +num to stack
# [3] 
# preOp = +, num = 0

# i = 2, s[2] = 2, an operand, so we'll be setting num
# preOp = +, num = 2
# [3]

# i = 3, s[3] = *, an operator, so we'll pushing to stack
# preOp = +, preOp is + so push 2 to stack, (stack top is at the left)
# [2, 3]
# set preOp as s[i], preOp = *, num = 0

# i = 4, s[4] = 2, an operand, so we'll be setting num
# preOp = *
# num = 2
# [2, 3]

# i = 5, s[5] = '+', an operator, so we'll pushing to stack
# preOp = *
# num = 2
# (pop 2) * n == 2 * 2 = 4 push into stack
# [4, 3]
# preOp = +, num = 0

# i = 6, s[6] = 0, an operand, so we'll be setting num
# num = 0, stack = [4,3]

# i = 7, out of bounds
# so we exit loop and sum the stack,
# sum([4, 3]) = 4 + 3 = 7

# Sample output for example:
# s: 3+2*2+0
# processing c: 3f
# is a digit so set num
# num: 3
# processing c: +
# is an op so push to stack
# stack: [3]
# processing c: 2
# is a digit so set num
# num: 2
# processing c: *
# is an op so push to stack
# stack: [3, 2]
# processing c: 2
# is a digit so set num
# num: 2
# processing c: +
# is an op so push to stack
# stack: [3, 4]
# processing c: 0
# is a digit so set num
# num: 0
# stack: [3, 4]

# Key Insights:
# 1. Our loop invariant is going to be that the stack always contains the numbers to be added
# 2. When current char is an operator, we push to stack based on previous operator, and set preOp = s[i] and num = 0
# 3. When current char is a digit we set num accordingly using base 10

# Example 2: s = "14-3/2"
# s: 14-3/2+0
# processing c: 1
# is a digit so set num
# num: 1
# processing c: 4
# is a digit so set num
# num: 14
# processing c: -
# is an op so push to stack
# stack: [14]
# processing c: 3
# is a digit so set num
# num: 3
# processing c: /
# is an op so push to stack
# stack: [14, -3]
# processing c: 2
# is a digit so set num
# num: 2
# processing c: +
# is an op so push to stack
# stack: [14, -1]
# processing c: 0
# is a digit so set num
# num: 0
# stack: [14, -1]

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(calculate("3+2*2"), 7)
assert_equal(calculate("14-3/2"), 13)