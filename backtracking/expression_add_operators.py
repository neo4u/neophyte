class Solution(object):
    def __init__(self):
        self.answer = []
        self.num = None
        self.target = None

    def addOperators(self, num: str, target: int) -> List[str]:
        self.num, self.n  = num, len(num)
        self.target = target
        self.recurse(0, 0, [], 0)

        return self.answer

    def recurse(self, index, value, ops, prev_val):
        # Base case. If we have considered all the digits
        if index == self.n:
            # And the value of the expression target, then we record this expression.
            if value == self.target: self.answer.append("".join(ops))
            return

        # This will keep track of the current operand. Remember that an operand is not necessarily equal
        # to a single digit.
        current_val = 0

        # Try all possible operands i.e. all suffixes num[index:] are operands.
        for i in range(index, self.n):

            # Current operand calculated on the fly rather than int(nums[index: i+1])
            current_val = current_val*10 + int(self.num[i])

            # If this is the first operand, we simple go onto the next recursion.
            if index == 0:
                self.recurse(i + 1, current_val, ops + [str(current_val)], current_val)
            else:
                # This is the value of the expression before the last operand came into the picture.
                # prev_val is the value of the previous operand with the appropriate sign (+ or -).
                v = value - prev_val

                # MULTIPLICATION will only be between previous value and the current value.
                self.recurse(i + 1, v + (prev_val * current_val), ops + ['*' + str(current_val)], prev_val * current_val)

                # Recurse by ADDING the current operand to the expression.
                self.recurse(i + 1, value + current_val, ops + ['+' + str(current_val)], current_val)

                # Recurse by SUBTRACTING the current operand to the expression.
                self.recurse(i + 1, value - current_val, ops + ['-' + str(current_val)], -current_val)

            # If a string starts with '0', then it has to be an operand on its own. We can't have '025' as an operand. That doesn't make sense
            if self.num[index] == '0': break


class Solution(object):
    def __init__(self):
        self.answer = []
        self.nums = None
        self.target = None

    def addOperators(self, nums, target):
        self.nums = nums
        self.n = len(nums)
        self.target = target
        self.bt(0, 0, [], 0)

        return self.answer

    def bt(self, index, value, ops, prev_val):
        if index == self.n:
            if value == self.target: self.answer.append("".join(ops))
            return

        current_val = 0
        for i in range(index, self.n):
            current_val = current_val*10 + int(self.nums[i])
            if index == 0:
                self.bt(i + 1, current_val, ops + [str(current_val)], current_val)
            else:
                self.bt(i + 1, value - prev_val + (prev_val * current_val), ops + ['*' + str(current_val)], prev_val * current_val)
                self.bt(i + 1, value + current_val, ops + ['+' + str(current_val)], current_val)
                self.bt(i + 1, value - current_val, ops + ['-' + str(current_val)], -current_val)

            if self.nums[index] == '0': break



# Time: O(n^2 * 3^n)
# Space: O(n^2 * 3^n)

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.num, self.target = num, target
        self.result, self.n = [], len(num)
        self.bt(0, 0, 0, [])
        return self.result

    def bt(self, idx, val, prev_val, ops):
        if idx == self.n:
            if val == self.target:
                self.result.append("".join(ops))
        else:
            curr_val = 0
            for i in range(idx, self.n):
                curr_val = 10 * curr_val + int(self.num[i])
                if idx == 0:
                    self.bt(i + 1, curr_val, curr_val, ops + [str(curr_val)])
                else:
                    v = val - prev_val
                    self.bt(i + 1, v + prev_val * curr_val, prev_val * curr_val, ops + ["*" + str(curr_val)])
                    self.bt(i + 1, val + curr_val, curr_val, ops + ["+" + str(curr_val)])
                    self.bt(i + 1, val - curr_val, -curr_val, ops + ["-" + str(curr_val)])

                if self.num[idx] == "0": break


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.num, self.target = num, target
        self.ans, self.n = [], len(self.num)
        if not self.num: return self.ans

        self.bt(1, 0, int(self.num[0]), int(self.num[0]), self.num[0])
        return self.ans

    def bt(self, i, total, prod, pre, path):
        cur = int(self.num[i])

        if i == self.n - 1:
            if total + prod + cur == self.target:
                self.ans.append(f'{path}+{self.num[i]}')
            if total + prod - cur == self.target:
                self.ans.append(f'{path}-{self.num[i]}')
            if total + prod * cur == self.target:
                self.ans.append(f'{path}*{self.num[i]}')
            if pre:
                cur = pre * 10 + cur
                if total + prod // pre * cur == self.target:
                    self.ans.append(f'{path}{self.num[i]}')
        else:
            self.bt(i + 1, total + prod, cur, cur, f'{path}+{self.num[i]}')
            self.bt(i + 1, total + prod, -cur, cur, f'{path}-{self.num[i]}')
            self.bt(i + 1, total, prod * cur, cur, f'{path}*{self.num[i]}')
            if pre:
                cur = pre * 10 + cur
                self.bt(i + 1, total, prod // pre * cur, cur, f'{path}{self.num[i]}')
