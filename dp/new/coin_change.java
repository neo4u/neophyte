// #Recursive Method:#
// The idea is very classic dynamic programming: think of the last step we take.
// Suppose we have already found out the best way to sum up to amount a, then for the last step,
// we can choose any coin type which gives us a remainder r where r = a-coins[i] for all i's.
// For every remainder, go through exactly the same process as before until either the
// remainder is 0 or less than 0 (meaning not a valid solution).
// With this idea, the only remaining detail is to store the minimum number of coins needed to
// sum up to r so that we don't need to recompute it over and over again.

// Code in Java:

public class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount<1) return 0;
        return helper(coins, amount, new int[amount]);
    }

    private int helper(int[] coins, int rem, int[] count) { // rem: remaining coins after the last step; count[rem]: minimum number of coins to sum up to rem
        if(rem<0) return -1; // not valid
        if(rem==0) return 0; // completed
        if(count[rem-1] != 0) return count[rem-1]; // already computed, so reuse
        int min = Integer.MAX_VALUE;
        for(int coin : coins) {
            int res = helper(coins, rem-coin, count);
            if(res>=0 && res < min)
                min = 1+res;
        }
        count[rem-1] = (min==Integer.MAX_VALUE) ? -1 : min;
        return count[rem-1];
    }
}


// #Iterative Method:#
// For the iterative solution, we think in bottom-up manner.
// Suppose we have already computed all the minimum counts up to sum,
// what would be the minimum count for sum+1?

// Code in Java:

public class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount<1) return 0;
        int[] dp = new int[amount+1];
        int sum = 0;
        
        while(++sum<=amount) {
            int min = -1;
            for(int coin : coins) {
                if(sum >= coin && dp[sum-coin]!=-1) {
                    int temp = dp[sum-coin]+1;
                    min = min<0 ? temp : (temp < min ? temp : min);
                }
            }
            dp[sum] = min;
        }
        return dp[amount];
    }
}

// If you are interested in my other posts,
// please feel free to check my Github page here:
// https://github.com/F-L-A-G/Algorithms-in-Java