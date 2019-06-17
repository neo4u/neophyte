# First sort the coins, we will deal with big coin first
# When there is no hope to reduce total count, stop the dfs

class Solution3:
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


class Solution2(object):
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


# dp[i] represents fewest number of coins making up amount i,
# transistion funciton
# then for every coin in coins, dp[i] = min(dp[i - coin] + 1, dp[i])
# dp[i] is number of coins without the current
# dp[i - coin] + 1 is the number of coins with the current coin
# The time complexity is O(amount * coins.length) and the space complexity is O(amount)
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c > i: continue
                dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]
