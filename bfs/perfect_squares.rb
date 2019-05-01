# # @param {Integer} n
# # @return {Integer}
def num_squares(n)
    return if n < 0
    return 1 if n == 0

    i, squares = 1, []
    while i * i <= n
        squares << i * i
        i += 1
    end

    # Mark the distance at 0 as 1
    q, visited = [[0, 1]], Set.new([0])
    while !q.empty?
        node, distance = q.shift
        squares.each do |square|
            tmp = square + node

            # Return the distance at current node
            return distance if tmp == n

            # We only add neighbours which are less than n
            break if tmp > n

            # Skip already considered sums of squares
            next if visited.include?(tmp)

            visited.add(tmp)

            # Add to queue and increment the distance of current level by 1
            q.push([tmp, distance + 1])
        end
    end

    # nil will be return in case of no square sum
end


# using System;

# public class Solution
# {
#     public int NumSquares(int n)
#     {
#         if (n <= 3) return n;

#         var dp = new int[n + 1];
#         dp[0] = 0;
#         dp[1] = 1;
#         dp[2] = 2;
#         dp[3] = 3;

#         for (int i = 4; i <= n; i++)
#         {
#             dp[i] = i; // i times (1*1) = i;

#             int min = int.MaxValue;
#             for (int j = 1; j * j <= i; j++) // find smaller
#             {
#                 min = Math.Min(min, dp[i - j * j] + 1);
#             }
#             dp[i] = min;
#         }

#         return dp[n];
#     }
# }


# https://leetcode.com/problems/perfect-squares/description/
# 279.Perfect Squares

# We can also view this question as a graph question if e treat each number from 1 to n as nodes.
# And there is an edge between two nodes i and j if and only if there exists and number k such that:
#   i = j + k * k or j = i + k * k, where k*k ≤ i and k*k ≤ j
# Hence, if we abstract this question into searching shortest path in a graph,
# we can also solve this question via BFS because of its suitability for searching shortest path.

# Controversial time complexity

# Time complexity: O(n^(n+1)) because in the worst case we can search n + 1 level in depth
# (worst case the perfect squares are made up all by 1s) from 0 and the tree can thus contains up to
#  n^(n+1) nodes (n^0 + n^1 + n^2 + ... + n^(n-1) + n^n).

# The time complexity is O(E + V) = O(n*n1/2 + n) since a node can have at most n^1/2 perfect square numbers that are <= n, and therefore n1/2 edges.
# Space complexity: O(n^n) because of the queue used to store each level we are iterating through.

# Space complexity: O(n^n) because of the queue used to store each level we are iterating through.


require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(num_squares(12), 3)
# assert_equal(num_squares(7168), 4)
