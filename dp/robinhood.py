# Portfolio Value Optimization - Robinhood

# You have some securities available to buy that each has a price buy_vals[i].
# Your friend predicts for each security the stock price will be sell_vals[i] at some future date. But based on volatility of each share,
# you only want to buy up to counts[i] shares of each security i.

# Given amount dollars to spend,
# calculate the maximum value you could potentially achieve based on the predicted prices sell_vals[i]
# (and including any cash you have remaining).


# Example 1:
# Input: amount = 140, buy_vals = [15, 40, 25, 30], sell_vals = [45, 50, 35, 25], counts = [3, 3, 3, 4])
# Output: 265 (with fractional buy)

# Example 2: 
# Input: Amount = 30, buy_vals = [15, 20], sell_vals = [30, 45], counts = [3, 3] == 67.5
# Output:
# For fractional: 67.5 (Buy 1.5 shares of the 20 value security)
# For non-fractional: 60 (Buy 2 shares of 15 value security)


# Feels like 0/1 Knapsack problem or Knapsack problem for fractional usage, I'm not good at DP and am having trouble coming up with a solution. Could the leetcode collective help?

# max_revenue(i, amount) = amount when i == n
# max(max_revenue(i - 1, amount - count * b_val) + count * (s_val - b_val) for count in range(A[i]) such that amount - count * b_val >= 0)
TAB = '\t'
def optimize_portfolio_without_fractionals(amount, b_vals, s_vals, counts):
    return dfs(0, amount, {}, b_vals, s_vals, counts)

def dfs(i, amount, memo, b_vals, s_vals, counts, depth=0):
    if i == len(b_vals): return amount
    print(f"{TAB * depth} dfs(i={i}, amount={amount}, i_val={b_vals[i]}, f_val={s_vals[i]})")

    if (i, amount) in memo:
        print(f"{TAB * depth} dfs(i={i} return from memo")
        return memo[(i, amount)]
    if b_vals[i] >= s_vals[i]:
        print(f"{TAB * depth} returning")
        return 0

    vals = []
    for count in range(counts[i] + 1):
        if amount < count * b_vals[i]: continue
        print(f"{TAB * depth} count: {count}, amount: {amount}")
        rev_from_rest = dfs(i + 1, amount - count * b_vals[i], memo, b_vals, s_vals, counts, depth + 1)
        vals.append(
            (rev_from_rest + count * s_vals[i], -b_vals[i])
        )
        max_val = max(vals)[0]
    print(f"{TAB * depth} revs: {vals}, max_rev: {max_val}")
    memo[(i, amount)] = max_val
    print(f"{TAB * depth} return: {max_val}")
    return max_val


def optimize_portfolio_with_fractionals(amount, b_vals, s_vals, counts):
    n = len(b_vals)
    sorted_arrs = [(s_val/b_val, b_val, s_val, c) for b_val, s_val, c in zip(b_vals, s_vals, counts)]
    sorted_arrs.sort(key=lambda x: x[0], reverse=True)
    b_vals = [sorted_arrs[i][1] for i in range(n)]
    s_vals = [sorted_arrs[i][2] for i in range(n)]
    counts = [sorted_arrs[i][3] for i in range(n)]
    revenue, i = 0, 0

    while amount > 0 and i < n:
        num_shares = min(amount/b_vals[i], counts[i])
        revenue += num_shares * s_vals[i]
        amount -= num_shares * b_vals[i]
        i += 1

    return revenue

assert optimize_portfolio_with_fractionals(30, [15, 20], [30, 45], [3, 3]) == 67.5
assert optimize_portfolio_without_fractionals(30, [15, 20], [30, 45], [3, 3]) == 60

assert optimize_portfolio_with_fractionals(140, [15, 40, 25, 30], [45, 50, 35, 25], [3, 3, 3, 4]) == 265
assert optimize_portfolio_without_fractionals(140, [15, 40, 25, 30], [45, 50, 35, 25], [3, 3, 3, 4]) == 255

assert optimize_portfolio_without_fractionals(35, [15, 20], [30, 45], [3, 3]) == 75
assert optimize_portfolio_without_fractionals(45, [15, 20], [30, 45], [3, 3]) == 95
assert optimize_portfolio_without_fractionals(10, [1, 2, 3, 4], [4, 3, 2, 1], [4, 3, 2, 1]) == 25
assert optimize_portfolio_without_fractionals(10, [1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 4]) == 10



# Code Review: Money Transfer
#
# Since our systems process billions of dollars in trades per week, it’s
# important that trade processing and money transfer are error-free.
#
# Suppose the code below comes to you for code review. The responsibility of
# this code block is to transfer money from one account to another
# and send emails to both account owners when the transfer is complete.
#
# This code is logically correct. However, given that we operate in the real
# world on a distributed system with millions of people transferring money in
# and out, what could go wrong? How would you change the code below to
# accommodate these failure scenarios?
#
# Don't focus on code style or refactoring the code.
#  src_account ---> dst_account
# . dst_account ---> src_account
# def bad_transfer(src_account, dst_account, amount):
#     src_cash = src_account.cash # DB read
#     dst_cash = dst_account.cash # DB read
#     if src_cash < amount:
#         raise InsufficientFunds

#     src_account.cash = src_cash - amount # DB write
#     dst_account.cash = dst_cash + amount # DB write

#     src_account.send_src_transfer_email()
#     dst_account.send_dst_transfer_email()