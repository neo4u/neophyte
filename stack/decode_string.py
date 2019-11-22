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
class SolutionDFS:
    def decodeString(self, s: str) -> str:
        self.pos = 0
        return self.dfs(s)

    def dfs(self, s):
        num, word = '', ''

        while self.pos < len(s):
            c = s[self.pos]
            self.pos += 1
            if c.isdigit(): num += c
            elif c == '[':  word += self.dfs(s) * int(num); num = ''
            elif c == ']':  return word
            else:           word += c
        return word



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
