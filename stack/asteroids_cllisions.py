from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < abs(ast):
                    stack.pop()
                    continue
                elif stack[-1] == abs(ast):
                    stack.pop()
                break
            else:
                stack.append(ast)

        return stack


# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/description/

# Example:

# [5, 10, -5]
# stack = []
# 5
# Stack is empty, so push to stack

# stack = [5]
# 10
# stack is not empty, but ast is non-neg've, so push to stack

# stack = [5, 10]
# -5
# stack is not emtpy and incoming ast is -ve and stack top is +ve
# but then value of incoming is lesser which means it will break on collision with top

# Hence we end up with [5, 10]

# Steps:
# - Use a stack to store all asteroid that don't collide, resolving collisions as we add to it.
# - So as long as stack is empty and we get a non-negative asteroid or stack top is negative, just push to stack
# - If at any point we have the conditions of non-empty stack and -ve incoming with  stack[-1] < abs(ast),
#   this means incoming will break the stack top, that's why we keep popping in a while loop
#   until ast doesn't collide with stack top and only then push it to stack
# - If at any point we have the condition of 
