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

# Approach 3: Iterative
# @param {Float} x
# @param {Integer} n
# @return {Float}
def my_pow_iter(x, n)
    m = n
    n = n.abs
    ans, curr, i = 1, x, n
    while i > 0
        ans *= curr if i % 2 == 1
        
        curr *= curr
        i /= 2
        puts "ans: #{ans} | curr: #{curr} | i: #{i}"
    end

    m < 0 ? 1/ans : ans
end

# def myPow(self, x, n):
#     m = abs(n)
#     ans = 1.0
#     while m:
#         if m & 1:
#             ans *= x
#         x *= x
#         m >>= 1
#     return ans if n >= 0 else 1 / ans

# def my_pow(x, n)
#     m = n.abs
#     ans = 1.0

#     while m > 0
#         ans *= x if m & 1
#         x *= x
#         m >>= 1
#     end

#     n < 0 ? 1/ans : ans
# end


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


require 'test/unit'
extend Test::Unit::Assertions


assert_equal(my_pow_iter(2, 2), 4)