# @param {Integer} n
# @return {Integer}
def num_trees(n)
    # F(i, n) is the number of trees with i as root for nodes 1...n
    # F(i, n) = G(i - 1) * G(n - i) where G(i - 1) is the number of left subtrees, G(n - i) is the no. of right subtrees
    dp = Array.new(n + 1, 0)
    dp[0] = dp[1] = 1
  
    2.upto(n) do |i|
      1.upto(i) do |j|
        dp[i] += dp[j - 1] * dp[i - j]
      end
    end

    dp[n]
end

# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/solution/

# Algorithm
# The problem is to calculate the number of unique BST. To do so, we can define two functions:

# G(n): the number of unique BST for a sequence of length n.
# F(i,n): the number of unique BST, where the number i is served as the root of BST (1 ≤ i ≤ n).

# As we can see,
# G(n) is actually the desired function we need in order to solve the problem.


# Time complexity: the main computation of the algorithm is done at the statement with G[i].
# So the time complexity is essentially the number of iterations for the statement,
# which is summation over i from 2 to n of (2+n)(n−1), to be exact, therefore the time complexity is O(N^2)
# Space complexity: The space complexity of the above algorithm is mainly the storage to keep all the intermediate solutions, therefore O(N)O(N).

# Another nice article for understanding
# https://www.quora.com/Given-n-how-many-structurally-unique-BSTs-binary-search-trees-that-store-values-1-to-n-are-there-How-would-I-come-up-with-the-solution-Can-you-explain-the-thought-process-that-leads-to-the-solution