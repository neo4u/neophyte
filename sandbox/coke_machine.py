class Solution:
    def cokeMachine(self, buttons, target):
        if not buttons: return False
        self.memo = set()
        return self.bt(buttons, (0, 0), target)

    def bt(self, buttons, curr_int_sum, target):
        if curr_int_sum in self.memo: return False
        if curr_int_sum[0] >= target[0] and curr_int_sum[1] <= target[1]: return True
        if curr_int_sum[1] > target[1]: return False

        for b in buttons:
            new_int = curr_int_sum[0] + b[0], curr_int_sum[1] + b[1]
            if self.bt(buttons, new_int, target): return True

        self.memo.add(curr_int_sum)
        return False

sol = Solution()
assert sol.cokeMatch([[100, 120], [200, 240], [400, 410]], [100, 110]) == False
assert sol.cokeMatch([[100, 120], [200, 240], [400, 410]], [90, 120]) == True
assert sol.cokeMatch([[100, 120], [200, 240], [400, 410]], [300, 360]) == True
assert sol.cokeMatch([[100, 120], [200, 240], [400, 410]], [310, 360]) == False
assert sol.cokeMatch([[100, 120], [200, 240], [400, 410]], [1, 9999999999]) == True

# https://leetcode.com/discuss/interview-question/307252/Google-onsite-Coke-Machine