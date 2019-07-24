// Now we can see that dp[i][j] only rely on dp[i-1][j] and dp[i][j-coins[i]], then we can optimize the space by only using one-dimension array.

class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int i = 1; i <= amount; i++) {
                if (i < coin) continue;
                dp[i] += dp[i-coin];
            }
        }
        return dp[amount];
    }
}

class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i < coin) continue;
                dp[i] += dp[i - coin];
            }
        }
        return dp[amount];
    }
}

// 5
// [1,2,5]

// dp [1, 1, 2, 3, 0, 0]

// 2     + 1
// 1 + 1 + 1

// 1     + 2