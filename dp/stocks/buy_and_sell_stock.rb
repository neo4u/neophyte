# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    return 0 if !prices || prices.empty?

    max_sum, cur_sum, n = 0, 0, prices.size()
    1.upto(n - 1) do |i|
        cur_sum = [0, cur_sum + prices[i] - prices[i - 1]].max
        max_sum = [max_sum, cur_sum].max
    end

    max_sum
end

# The logic to solve this problem is same as "max subarray problem" using Kadane's Algorithm. Since no body has mentioned this so far, I thought it's a good thing for everybody to know.
# All the straight forward solution should work, but if the interviewer twists the question slightly by giving the difference array of prices, Ex: for {1, 7, 4, 11}, if he gives {0, 6, -3, 7}, you might end up being confused.
# Here, the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) of the original array, and find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.
# Time: O(n)
# Space: O(1)