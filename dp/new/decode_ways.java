public class Solution {
    public int numDecodings(String s) {
        if(s == null || s.length() == 0) {
            return 0;
        }
        int n = s.length();
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = s.charAt(0) != '0' ? 1 : 0;
        for(int i = 2; i <= n; i++) {
            int first = Integer.valueOf(s.substring(i-1, i));
            int second = Integer.valueOf(s.substring(i-2, i));
            if(first >= 1 && first <= 9) {
               dp[i] += dp[i-1];  
            }
            if(second >= 10 && second <= 26) {
                dp[i] += dp[i-2];
            }
        }
        return dp[n];
    }
}

// I used a dp array of size n + 1 to save subproblem solutions. dp[0] means an empty 
// string will have one way to decode, dp[1] means the way to decode a string of size 1.
// I then check one digit and two digit combination and save the results along the way.
// In the end, dp[n] will be the end result.

// visulization
// 102213 ————— 5
// 10221 3
// 1022 13

// \\\\\\\\\
// 10221————— 3
// 1022 1
// 102 21

// \\\\\\\\
// 1022 —————— 2
// 102 2
// 10 22

// \\\\\
// 102———— 1
// 10 2
// 1 02

// \\\\\\\\
// 10—————— 1
// 1 0
// 10

// Great idea! It's right to initialize dp[0] as 1, but it's not accurate to say ''an empty string will have one way to decode''. In dynamic programming, we usually set dp[0] = 1.
// For example, say the sequence is '10', we have dp[1] = 1. Then checking the second digit '0', we have dp[2] = 0 after the first ''if'' condition, then in the second ''if'' condition, we have dp[2] += dp[0], here we should have dp[2] = 1, which means dp[0] should be 1.
// And whenever we encounter dp[i] = 0, which means the sub-sequence from the beginning to current position is not decodable, we can return 0. This may avoid unnecessary computation.

// Evolving solutions
public class Solution {

    // Recursion O(2^n)
    int numDecodings(string s) {
        return s.empty() ? 0: numDecodings(0,s);    
    }
    int numDecodings(int p, string& s) {
        int n = s.size();
        if(p == n) return 1;
        if(s[p] == '0') return 0;
        int res = numDecodings(p+1,s);
        if( p < n-1 && (s[p]=='1'|| (s[p]=='2'&& s[p+1]<'7'))) res += numDecodings(p+2,s);
        return res;
    }

    // Memoization O(n)
    int numDecodings(string s) {
        int n = s.size();
        vector<int> mem(n+1,-1);
        mem[n]=1;
        return s.empty()? 0 : num(0,s,mem);   
    }
    int num(int i, string &s, vector<int> &mem) {
        if(mem[i]>-1) return mem[i];
        if(s[i]=='0') return mem[i] = 0;
        int res = num(i+1,s,mem);
        if(i<s.size()-1 && (s[i]=='1'||s[i]=='2'&&s[i+1]<'7')) res+=num(i+2,s,mem);
        return mem[i] = res;
    }

    // dp O(n) time and space, this can be converted from #2 with copy and paste.
    int numDecodings(string s) {
        int n = s.size();
        vector<int> dp(n+1);
        dp[n] = 1;
        for(int i=n-1;i>=0;i--) {
            if(s[i]=='0') dp[i]=0;
            else {
                dp[i] = dp[i+1];
                if(i<n-1 && (s[i]=='1'||s[i]=='2'&&s[i+1]<'7')) dp[i]+=dp[i+2];
            }
        }
        return s.empty()? 0 : dp[0];   
    }

    // dp constant space
    int numDecodings(string s) {
        int p = 1, pp, n = s.size();
        for(int i=n-1;i>=0;i--) {
            int cur = s[i]=='0' ? 0 : p;
            if(i<n-1 && (s[i]=='1'||s[i]=='2'&&s[i+1]<'7')) cur+=pp;
            pp = p;
            p = cur;
        }
        return s.empty()? 0 : p;   
    }
}