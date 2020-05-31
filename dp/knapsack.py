# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(w, weights, vals):
    n = len(vals)
    dp = [[0 for j in range(w + 1)] for i in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(vals[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][w]


# dp[i][j] represents, max value formed by values[0:i-1] with weight j
# dp[i][j] = max| vals[i] + dp[i - 1][j - weights[i]]
#               | dp[i - 1][j]

# assert knapSack(50, [10, 20, 30], [60, 100, 120]) == 220
# assert knapSack(30, [15, 20], [30, 45]) == 60





# dp[i][j] represents, max value formed by i_vals[0:i-1] with amount j
# dp[i][j] = max| vals[i] + dp[i - 1][j - weights[i]]
#               | dp[i - 1][j]

def max_value(amount, i_vals, f_vals, counts):
    n = len(i_vals)
    dp = [[0 for j in range(amount + 1)] for i in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if i_vals[i - 1] <= j:
                dp[i][j] = max(f_vals[i - 1] + dp[i - 1][j - i_vals[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][amount]


# dp[i] represents max value you can get for weight i

def optimize_portfolio_without_fractionals(w, vals, weights, counts):
    dp = [0 for i in range(w + 1)]

    # TODO Try to divide all elements by the smallest element, to
    # decrease the space requirement

    for i in range(1, w + 1):
        dp[i] = dp[i - 1]
        for j, val in enumerate(vals):
            if weights[j] <= i and dp[i] < dp[i - weights[j]] + val and counts[j] != 0:
                dp[i] = dp[i - weights[j]] + val
                counts[j] -= 1
    return dp[w]



# Example 2:
# Input:
# M = $30
# P1=15, S1=30, A1=3 (AAPL)
# P2=20, S2=45, A2=3 (TSLA)

# Output:
# When buying fractionals,
# Buy 1.5 shares of TSLA ($67.5 value)

# When buying whole shares,
# Buy 2 shares of AAPL ($60 value)


assert optimize_portfolio_without_fractionals(10, [7, 16], [5, 10], [3, 3]) == 60
assert optimize_portfolio_with_fractionals(10, [7, 16], [5, 10], [3, 3]) == 67.5
