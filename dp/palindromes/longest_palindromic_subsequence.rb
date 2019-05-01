
# public class Solution {
#     public int longestPalindromeSubseq(String s) {
#         int[][] dp = new int[s.length()][s.length()];
        
#         for (int i = s.length() - 1; i >= 0; i--) {
#             dp[i][i] = 1;
#             for (int j = i+1; j < s.length(); j++) {
#                 if (s.charAt(i) == s.charAt(j)) {
#                     dp[i][j] = dp[i+1][j-1] + 2;
#                 } else {
#                     dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
#                 }
#             }
#         }
#         return dp[0][s.length()-1];
#     }
# }

# 516. Longest Palindromic Subsequence
# https://leetcode.com/problems/longest-palindromic-subsequence/description/

# dp[i][j]: the length of longest palindromic subsequence in substring s(i, j), here i, j represent left, right indexes in the string
# State transition:
# dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
# otherwise, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
# Initialization: dp[i][i] = 1

# "cbbd"
# d

# b
# bd

# b
# bb
# bbd

# c
# cb
# cbb
# cbbd
  

# c  1 0 0 0
# b  0 1 2 2
# b  0 0 1 1
# d  0 0 0 1



# int longestPalindromeSubseq(string s) {
#     int n = s.size();
#     vector<vector<int>> dp(n+1,vector<int>(n));
    
#   for(int i=0;i<n;i++)
#   {
#     dp[1][i] = 1
#   };
  
#     for(int len=2; len <= n; len++) //length
#     { 
#         for(int i = 0; i < n - len + 1; i++) //start index
#         {							 
#             if s[i] == s[i + len - 1]
#                 dp[len][i] = dp[len - 2][i + 1] + 2
#             else
#                 dp[len][i] = max(dp[len - 1][i], dp[len - 1][i + 1]);
#         }
#     }  
  
#    return dp[n][0]; 
# }

# cbbd

# dp[2,0]
# cb
# dp[2,1]
# bb
# dp[2,2]
# bd

# dp[3, i]
# dp[3,0] = cbb max{cb, bb}
# dp[3,1] = bbd max{bb, db}
# dp[3,2] = out of bound

# dp[4, i]
# dp[4,0] = cbbd max{cbb, bbd}
# dp[4,1] = out of bound

# 0 0 0 0
# 1 1 1 1
# 1 2 1 0
# 2 2 0 0
# 2 0 0 0