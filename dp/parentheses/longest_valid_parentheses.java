// Stack solution 10ms
// The idea is simple, we only update the result (max) when we find a "pair".
// If we find a pair. We throw this pair away and see how big the gap is between current and previous invalid.
// EX: "( )( )"
// stack: -1, 0,
// when we get to index 1 ")", the peek is "(" so we pop it out and see what's before "(".
// In this example it's -1. So the gap is "current_index" - (-1) = 2.

// The idea only update the result (max) when we find a "pair" and push -1 to stack first covered all edge cases.

public class Solution {
    public int longestValidParentheses(String s) {
        LinkedList<Integer> stack = new LinkedList<>();
        int result = 0;
        stack.push(-1);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ')' && stack.size() > 1 && s.charAt(stack.peek()) == '(') {
                stack.pop();
                result = Math.max(result, i - stack.peek());
            } else {
                stack.push(i);
            }
        }
        return result;
    }
}
// //DP solution 4ms
// The idea is go through the string and use DP to store the longest valid parentheses at that point.
// take example "()(())"
// i : [0,1,2,3,4,5]
// s : [( ,) ,( ,( ,) ,) ]
// DP:[0,2,0,0,2,6]

// 1, We count all the ‘(‘.
// 2, If we find a ‘)’ and ‘(‘ counter is not 0, we have at least a valid result size of 2. “()"
// 3, Check the the one before (i - 1). If DP[i - 1] is not 0 means we have something like this “(())” . This will have DP “0024"
// 4, We might have something before "(())”. Take "()(())” example, Check the i = 1 because this might be a consecutive valid string.

public class Solution {
    public int longestValidParentheses(String s) {
        int[] dp = new int[s.length()];
        int result = 0;
        int leftCount = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                leftCount++;
            } else if (leftCount > 0){
                dp[i] = dp[i - 1] + 2;
                dp[i] += (i - dp[i]) >= 0 ? dp[i - dp[i]] : 0;
                result = Math.max(result, dp[i]);
                leftCount--;
            }
        }
        return result;
    }
}