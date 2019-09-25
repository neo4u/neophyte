# Approach 1: Iterative using Stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack, num = [["", 1]], ""

        for c in s:
            if c.isdigit(): num += c
            elif c == '[':
                stack.append(["", int(num)])
                num = ""
            elif c == ']':
                top_num, count = stack.pop()
                stack[-1][0] += top_num * count
            else:
                stack[-1][0] += c

        return stack[-1][0]


# Approach 2: Recursive
class SolutionRecurse:
    def decodeString(self, s: str) -> str:
        return self.recurse(list(s))

    def recurse(self, s):
        result = ""

        while s:
            num = ""
            while s and s[0].isdigit(): num += s.pop(0)

            if num:
                num = int(num)
                s.pop(0)
                result += self.recurse(s) * num
            else:
                c = s.pop(0)
                if c not in "[]": result += c
                if c == ']': break

        return result


# 394. Decode String
# https://leetcode.com/problems/decode-string/description/


# Intuition
# 1. The tricky part here is the nested chars
# 2. We can use recursion, or iteratively we can use stack to simulate the recursion ourselves


# Approach 1: Stack, Iterative
# Steps:
# 1. We'll use stack and initialize it with current string ""
#    and the repitition count of 1, ["", 1] will be the bottom of the stack
# 2. Each time we hit a '[', means we've contructed the rep count,
#    so we add an item in the stack with an empty string and repitition count
# 3. As long as we see a digit keep constructing the digit
# 4. As long as its a alphabet char keep appending to the string part of the top item on stack
# 5. As soon as we see a ']', we pop the top item and
#    multiply the string part with the count part and add to top of stack

