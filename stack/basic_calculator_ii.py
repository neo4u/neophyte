class Solution:
    def calculate(self, s):
        s += '+0'
        stack, num, preOp = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit(): num = num * 10 + int(s[i])
            elif not s[i].isspace():
                if   preOp == "-":  stack.append(-num)
                elif preOp == "+":  stack.append(num)
                elif preOp == "*":  stack.append(stack.pop() * num)
                else:               stack.append(int(stack.pop() / num))
                preOp, num = s[i], 0
        return sum(stack)



# Example: "3+2*2+0"
# i = 0, s[0] = 3, an operand, so we'll be setting n
# preOp = +, n = 3
# []

# i = 1, s[1] = +, an operator, so we'll be pushing to stack
# preOp = +, n = 3
# push +num to stack
# [3] 
# preOp = +, n = 0

# i = 2, s[2] = 2, an operand, so we'll be setting n
# preOp = +, n = 2
# [3]

# i = 3, s[3] = *, an operator, so we'll pushing to stack
# preOp = +, preOp is + so push 2 to stack, (stack top is at the left)
# [2, 3]
# set preOp as s[i], preOp = *, n = 0

# i = 4, s[4] = 2, an operand, so we'll be setting n
# preOp = *
# n = 2
# [2, 3]

# i = 5, s[5] = '+', an operator, so we'll pushing to stack
# preOp = *
# n = 2
# (pop 2) * n == 2 * 2 = 4 push into stack
# [4, 3]
# preOp = +, n = 0

# i = 6, s[6] = 0, an operand, so we'll be setting n
# n = 0, stack = [4,3]

# i = 7, out of bounds
# so we exit loop and sum the stack,
# sum([4, 3]) = 4 + 3 = 7

# Key Insights:
# 1. Our loop invariant is going to be that the stack always contains the numbers to be added
# 2. When current char is an operator, we push to stack based on previous operator, and set preOp = s[i] and n = 0
# 3. When current char is a digit we set n accordingly using base 10
