/**
 * dp[i] represents the total probability to get points i
 * dp[i] = dp[1] * 1/W + dp[2] * 1/W + dp[3] * 1/W + ... dp[i-2] * 1/W + dp[i-1] * 1/W
 * So dp[i] = (dp[1] + dp[2] + ... + dp[i - 1]) / W = Wsum / W
 * Conditional probability: keep a window with size K (assume K = 10), the probability of getting point i is the sum
 * of probability from point i - 10 to i, point i - 9 to i, ... , i -1 to i. Since every card has equal probability,
 * the probability to get any one of cards is 1/10. So the total probability of dp[i] is sum of all conditional
 * probability.
 * Once i is over than or equal to K, we can accumulate probability to final result
 * */
public double new21Game(int N, int K, int W) {
    if (K == 0 || N >= K + W) {
        return 1;
    }

    double result = 0;
    double Wsum = 1;
    double dp[] = new double[N + 1];
    dp[0] = 1;

    for (int i = 1; i <= N; i++) {
        dp[i] = Wsum / W;
        // when points is less than K, all previous card could go to current i by only drawing one card
        if (i < K) {
            Wsum += dp[i];
        }
        // when points is equal to or more than K, all probability will be accumulated to results
        else {
            result += dp[i];
        }

        // when i is over than W, then we need to move the window
        if (i - W >= 0) {
            Wsum -= dp[i - W];
        }
    }
    return result;
}