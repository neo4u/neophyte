require 'set'

def coin_change_bfs(coins, amount)
    return 0 if amount.zero?

    q, visited = [[0, 0]], Set.new([0])
    while !q.empty?
        node, dist = q.shift

        coins.each do |coin|
            nxt_node = coin + node
            return dist + 1 if nxt_node == amount
            next if nxt_node > amount
            next if visited.include?(nxt_node)

            visited.add(nxt_node)
            q.push([nxt_node, dist + 1])
        end
    end

    -1
end

def coin_change_dfs(coins, amount)
    memo = {}
    res = dfs(coins, amount, memo)
    res == Float::INFINITY ? -1 : res
end

def dfs(coins, amount, memo)
    return 0 if amount == 0
    return memo[amount] if memo[amount]

    res = Float::INFINITY
    coins.each do |coin|
        next if amount < coin
        sub_res = dfs(coins, amount - coin, memo)
        res = [res, sub_res + 1].min
    end

    memo[amount] = res
end

# Approach 3: DP bottom-up
# Clearer Code, DP Soltion
def coin_change(coins, amount)
    return 0 if amount == 0
    dp = Array.new(amount + 1, Float::INFINITY)
    dp[0] = 0

    coins.each do |coin|
        1.upto(amount).each do |i|
            next if i < coin
            dp[i] = [dp[i], dp[i - coin] + 1].min
        end
    end

    dp[amount] == Float::INFINITY ? -1 : dp[amount]
end

# Fastest solution
def coin_change(coins, amount)
    dp = Array.new(amount + 1, -1)
    dp[0] = 0
    
    coins.each do |c|
        puts "dp: #{dp}"
        1.upto(amount) do |i|
            next if i < c || dp[i - c] == -1
            dp[i] = dp[i - c] + 1 if dp[i] == -1 || dp[i - c] + 1 < dp[i]
            puts "\ti: #{i} dp: #{dp} dp[i - c]: #{dp[i - c]}"
        end
    end

    dp[amount]
end



# 322. Coin Change
# https://leetcode.com/problems/coin-change/


# Approach 1: BFS
# Time: O(n)
# Space: O(n)


# Approach 2: Recursion with memo (DP Top-Down)
# Time: O(amount * n)
# Space: O(amount)

# Approach 3: DP (DP Bottom-Up)
# Steps:
# 1. We try to form the amount with every coin
# 2. We take the min to form a previous amount (i - c) and check if dp[i - c] + 1 < dp[i], then update

# dp[i] represents the min number of coins to make up amount i
# Base case:
# dp[0] = 0, which means that it takes a minimum 0 coins of any type to form amount 0

# Recurrance relation:
# for every coin in coins, dp[i] = min(dp[i - coin] + 1)
# Meaning:
# 1. We take min coins required to form amount (i - coin) and add 1, for all amounts from 1 upto given amount
# 2. We update dp[i] with that amount if it is lesser than curr dp[i]

# Example:
# coin = [1, 2], amount = 3

# If 1 coin wasn't given, it'd have been bad. cuz of below flow.
# c: 2
# i = 1
# idx:    0       1       2                 3
# dp:     0       i < c   dp[2 - 1] == -1   dp[3 - 2] == -1
#         0       -1      -1                -1

# But since we have 1 coin, it'll look something like this.
# c = 1
# i:      0       1       2      3
# bfore:  0      -1      -1     -1
# dp:     0       1       2      3 [Just dp[i - 1] for each i, pretty simple

# c: 2
# i:      0       1       2                 3
# dp:     0       i < c   dp[2 - 2] == 0   dp[3 - 2] == 1
#         0       1       0 + 1            1 + 1

# We return dp[3] == 2

# printed from code
# dp: [0, -1, -1, -1]
#         i: 1 dp: [0, 1, -1, -1] dp[i - coin]: 0
#         i: 2 dp: [0, 1, 2, -1] dp[i - coin]: 1
#         i: 3 dp: [0, 1, 2, 3] dp[i - coin]: 2
# dp: [0, 1, 2, 3]
#         i: 2 dp: [0, 1, 1, 3] dp[i - coin]: 0
#         i: 3 dp: [0, 1, 1, 2] dp[i - coin]: 1

# Time: O(amount * n)
# Space: O(amount)


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(coin_change_bfs([186,419,83,408], 6249), 20)
assert_equal(coin_change_bfs([1,2,5], 11), 3)
assert_equal(coin_change_bfs([2], 3), -1)

assert_equal(coin_change_dfs([186,419,83,408], 6249), 20)
assert_equal(coin_change_dfs([1,2,5], 11), 3)
assert_equal(coin_change_dfs([2], 3), -1)

# assert_equal(coin_change_dp([186,419,83,408], 6249), 20)
# assert_equal(coin_change_dp([1,2,5], 11), 3)
# assert_equal(coin_change_dp([2], 3), -1)
assert_equal(coin_change_dp([1, 2], 3), 2)
