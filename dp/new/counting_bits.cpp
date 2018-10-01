// There is one imporant observation we can make about the number of bits in each number.

// Each Power of 2 has exactly only 1 bit. (2 : 0010 , 4: 0100, 8:1000, 16:10000)
// Each number after the power of 2 follows a pecular pattern :
// 0 → 0
// 1 → 0
// 2 → 1 + dp[0] Nearest Power of 2
// 3 → 1 + dp[1] 1 greater than nearest
// 4 → 1 + dp[0] Nearest
// 5 → 1+ dp[1] 1 greater than nearest
// 6 → 1+ dp[2] 2 greater than nearest
// 7 → 1+ dp[3] 3 greater than nearest
// 8 → 1+ dp[0] Nearest
// 9 → 1+ dp[1]
// 10 → 1+ dp[2]
// 11 → 1+ dp[3]
// 12 → 1+ dp[4]
// You can easily see the pattern here.

class Solution {
public:
    //Function to check whether the number is a power of 2 or now
    inline bool ispowerof2(int n){
        return (n & (n-1)) == 0; // If you include zero n && !(n & (n - 1)) or if you don't n > 0 && n & (n - 1)
    }

    vector<int> countBits(int num) {
        vector<int> dp(num+1);
        dp[0]=0;
        if(num>=1) 
            dp[1]=1;
        int curr=2;
        int nearest=2;
        while(curr<=num)
        {
            //nearest stores the nearest power of 2 less than current element (nearest of 5 is 4, nearest of 13 is 8..)
            nearest = ispowerof2(curr) ? curr  : nearest; 
            dp[curr] = 1 + dp[curr-nearest]; // 1 stands for dp[nearest]
            curr++;
        }
        return dp;
    }
};

// Just take note of the bool ispowerof2(n) method here. It uses bit operation to find whether it is power of 2. More tricks here. The reference is here
// Inline function is used for small functions which make the function code to be written at the call during compile time. It reduces overhead
// Hope you guys like the solution!