# @param {Float} x
# @param {Integer} n
# @return {Float}
def my_pow(x, n)
    return 0 if x == 0 
    return 1 if n == 0 
    return 1 / my_pow(x, -n) if n < 0
    
    half = my_pow(x, n/2)
    half_half = half * half 
    n.even? ? half_half : half_half * x
end


# Concise looking solution
# if n is odd it automatically does half * half * x
# if n is even it does half * half * 
# # @param {Float} x
# # @param {Integer} n
# # @return {Float}
def my_pow(x, n)
    return 1 if n == 0
    return x if n == 1
    return 0 if x == 0
    return 1 / my_pow(x, -n) if n < 0

    my_pow(x, n / 2) * my_pow(x, n / 2) * my_pow(x, n % 2)
end


# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

# O(n) multiply one by one 
# O(logn) divide and conquer
# x^n = x^(n/2) * x^(n/2) * optionally x
# special, negative, x=0, n=0 