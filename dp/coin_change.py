# First sort the coins, we will deal with big coin first
# When there is no hope to reduce total count, stop the dfs

class Solution:
    def coinChange(self, coins, amount):
        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res - count): # if hope still exists
                    dfs(i, rem - coins[i], count + 1)

        coins.sort(reverse = True)
        lenc, self.res = len(coins), float("inf")

        for i in range(lenc):
            dfs(i, amount, 0)

        return self.res if self.res < float("inf") else -1


class Solution(object):
    def helper(self, coins, amount, cache):
        if amount == 0:
            return 0
        elif amount in cache:
            return cache[amount]
        cache[amount] = float('inf')
        for c in coins:
            if amount - c >= 0:
                cache[amount] = min(cache[amount], self.helper(coins, amount-c, cache) + 1)
        return cache[amount]
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        elif min(coins) > amount:
            return -1
        else:
            coins.sort(reverse=True)
            answer = self.helper(coins, amount, {})
            return answer if answer != float('inf') else -1


# DP bottom-up
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = amount + 1
        coins.sort(reverse=True)
        dp = [MAX]*(MAX)
        dp[0] = 0
        for i in range(1, MAX):
            dp[i] = min([dp[i-c] if i>=c else (MAX) for c in coins]) ### List Comprehension is faster
            dp[i] = dp[i] + 1 if dp[i] != MAX else dp[i]
        return -1 if (dp[-1] == MAX) else dp[-1]

# Assume dp[i] is the fewest number of coins making up amount i,
# then for every coin in coins, dp[i] = min(dp[i - coin] + 1).
# The time complexity is O(amount * coins.length) and the space complexity is O(amount)
class Solution(object):
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        table = [amount + 1] * (amount+1)
        table[0] = 0
        for i in range(1,amount + 1):
            for coin in coins:
                if i >= coin:
                    table[i] = min(table[i],table[i-coin] + 1)
        if table[amount] > amount:
            return -1
        else:
            return table[amount]
    
# the most important part of this problem is to find the transition,
# F(n) = min(F(n-Ci)) + 1: Ci is every denomination in the coins.
# Then if we want to use top-bottom, we just use the recrusion, and
# Note: every time we have to check if the F(n-Ci) has already been computed
# (we will store it in a table).
# If we want to use bottom up, we just calculate from the base case.
# Note: if using python, there will be risks for time exceding limit problem.
# use table = [amount + 1] * (amount +1) instead of [amount +1 for i in range(amount + 1)].
# use for coin in coins instead of for i in range(len(coins))


# Method:

# Use dynamic programming approach to break this problem down to subproblems
# We optimally solve each subproblems, building upto the original problem
# 1. Subproblems: Min change for amount less than the original amount, building from amount of 0 upto the original amount with increments of 1. There are O(amount) subproblems.
#    No guessing here. Base case is when we have 0 amount which corresponds to 0 # of coins
# 2. Recurrence: Let DP[i] be the min # of coins for amount "i".
#    Then it follows that
#    DP[i] = min(DP[i-coins[0]), 
#    DP[i-coins[1],.....DP[i-coins[j])+1
#    for all j in range(0,len(coins)) and for all j such that
#    i-coins[j] >= 0 (that you can pay that coinage).
#    Using the above relationship, we can build DP[i] from bottom up starting from i=0 all the way to i=amount
# 3. Time: time/subproblem -> O(# of type of coins).
#    Total time: subproblems * time / subproblem = O(amount*# of type of coins)
#    Solves original problem ? Yes: Because DP[amount] is the answer