# Approach 1: Recursive
# @param {Float} x
# @param {Integer} n
# @return {Float}
def my_pow(x, n)
    return 0 if x == 0
    return 1 if n == 0
    return 1 / my_pow(x, -n) if n < 0

    half = my_pow(x, n / 2)
    half_half = half * half
    n.even? ? half_half : half_half * x  # exmaple 2 ^ 7 = (2 ^ 3) * (2 ^ 3) * 2
end

# Approach 2: Iterative
# @param {Float} x
# @param {Integer} n
# @return {Float}
def my_pow(x, n)

end


# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

# Approach 1: Brute-Force, O(n) multiply one by one

# Approach 2: Fast Power Algorithm Recursive
# Time: O(log(n)). Each time we apply the formula (x ^ n) ^ 2 = x ^ (2∗n), n is reduced by half.
#       Thus we need at most O(log(n)) computations to get the result.
# Space: O(log(n)). For each computation, we need to store the result of x^n/2.
#        We need to do the computation for O(log(n)) times, so the space complexity is O(log(n)).

# O(logn) 
# x^n = x^(n/2) * x^(n/2) * optionally x
# special, negative, x=0, n=0

# Approach 3: Fast Power Algorithm Iterative
# There is a O(log(n)) time and O(1) space algorithm 
# class Solution {
#     public double myPow(double x, int n) {
#         long N = n;
#         if (N < 0) {
#             x = 1 / x;
#             N = -N;
#         }
#         double ans = 1;
#         double current_product = x;
#         for (long i = N; i > 0; i /= 2) {
#             if ((i % 2) == 1) {
#                 ans = ans * current_product;
#             }
#             current_product = current_product * current_product;
#         }
#         return ans;
#     }
# };