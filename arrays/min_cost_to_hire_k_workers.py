class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        ans = float('inf')

        N = len(quality)
        for captain in range(N):
            # Must pay at least wage[captain] / quality[captain] per qual
            factor = Fraction(wage[captain], quality[captain])
            prices = []
            for worker in range(N):
                price = factor * quality[worker]
                if price < wage[worker]: continue
                prices.append(price)

            if len(prices) < K: continue
            prices.sort()
            ans = min(ans, sum(prices[:K]))

        return float(ans)

# 857. Minimum Cost to Hire K Workers
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

sol = Solution()
assert sol.mincostToHireWorkers([10,20,5], [70,50,30], 2) == 105.00000
assert sol.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3) == 30.666666666666668
