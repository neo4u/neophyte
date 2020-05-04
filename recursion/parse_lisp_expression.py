from typing import List


# Approach 1: Recursion
class Solution:
    def evaluate(self, expression: str) -> int:
        return int(self.calc(expression))

    def calc(self, expr: str, m: dict = {}) -> str:
        first_token = expr[0]
        if first_token != '(':
            if first_token in '-0123456789': return expr    # For number
            return m[expr]                                  # For variable

        expr = expr[1:-1]                                   # Remove outer braces and evaluate the expr
        cmd, expr = expr.split(' ', 1)
        args = self.split_args(expr)                        # Split top level expressions only into args split across spaces

        if cmd == 'add':    return str(int(self.calc(args[0], m)) + int(self.calc(args[1], m)))
        elif cmd == 'mult': return str(int(self.calc(args[0], m)) * int(self.calc(args[1], m)))
        elif cmd == 'let':
            new_m = dict(m) # NOTE: new dict for a new let expression, so that we don't have to remove when we exit current scope
            for i in range((len(args) - 1) // 2):
                new_m[args[2*i]] = self.calc(args[2*i + 1], new_m) # 0, 2, 4... are vars, 1, 3, 5... are expressions that need calc from left to right
            return self.calc(args[-1], new_m)

    def split_args(self, expr: str) -> List[str]:
        stack, result, start = 0, [], 0

        for i, c in enumerate(expr):
            if c.isspace() and not stack:
                result.append(expr[start:i])
                start = i + 1
            if c == '(':    stack += 1
            elif c == ')':  stack -= 1

        result.append(expr[start:]) # Append remaining from start to end
        return result


# Approach 2: Stack
# class Solution:
#     def __init__(self):
#         self.scopes = []
#         self.operators = ['add', 'mult', 'let']

#     def get_val(self, name):
#         for scope in reversed(self.scopes):
#             if name not in scope: continue
#             return scope[name]

#     def is_var(self, name):
#         return self.get_val(name) is not None

#     def perform_op(self, operator, operands):
#         operands = [self.get_val(operand) if self.is_var(operand) else operand for operand in operands]
#         if operator == 'let':
#             self.scopes.pop()
#             return operands[0]
#         elif operator == 'add':     return str(int(operands[0]) + int(operands[1]))
#         elif operator == 'mult':    return str(int(operands[0]) * int(operands[1]))

#     def evaluate(self, expression: 'str') -> 'int':
#         tokens = expression.replace('(', '( ').replace(')', ' )').split(' ') 
#         eval_stack, operators_stack, var_to_set = [], [], None

#         for token in tokens:
#             if token != ')':
#                 if token in self.operators:
#                     operators_stack.append(token)
#                     if token == 'let':
#                         self.scopes.append({})
#                         var_to_set = None
#                 elif operators_stack and operators_stack[-1] == 'let':
#                     if var_to_set is not None:
#                         if token != '(':
#                             self.scopes[-1][var_to_set] = self.get_val(token) if self.is_var(token) else token
#                             var_to_set = None
#                     else:
#                         var_to_set = token
#                 eval_stack.append(token)
#             elif token == ')':
#                 operands = []
#                 while not eval_stack[-1] in self.operators:
#                     operands.append(eval_stack.pop())
#                 operator = eval_stack.pop()

#                 eval_stack.pop()  # remove the '('
#                 operators_stack.pop()  # remove the current operator

#                 result = self.perform_op(operator, operands)
#                 eval_stack.append(result)
#                 if operators_stack and operators_stack[-1] == 'let' and var_to_set is not None:
#                     self.scopes[-1][var_to_set] = result
#                     var_to_set = None

#         return int(eval_stack.pop())


# 736. Parse Lisp Expression
# https://leetcode.com/problems/parse-lisp-expression/description/


# Approach 1: Recursion
# - This problem seems to naturally lend itself to a recursive appraoch as it has nested expression
# - In my head seems similar to basic calculator although implementation might turn out differently


# Approach 2: Stack
# - If we can use recursion, we should be able to use a stack and reproduce the results
# 


sol = Solution()
assert sol.evaluate('(add 1 2)') == 3
assert sol.evaluate('(mult 3 (add 2 3))') == 15
assert sol.evaluate('(let x 2 (mult x 5))') == 10

assert sol.evaluate('(let x 2 (mult x (let x 3 y 4 (add x y))))') == 14
assert sol.evaluate('(let x 3 x 2 x)') == 2
assert sol.evaluate('(let x 1 y 2 x (add x y) (add x y))') == 5
assert sol.evaluate('(let x 2 (add (let x 3 (let x 4 x)) x))') == 6
assert sol.evaluate('(let a1 3 b2 (add a1 1) b2)') == 4
