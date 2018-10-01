// DFS or backtracking whatever
public class Solution {
    public int numDistinct(String S, String T) {
        if (S == null || T == null) {
            return -1;
        } else if (T.isEmpty()) {
            return 1;
        } else if (S.isEmpty()) {
            return 0;
        }
       
         int cnt = 0;
         for (int i = 0; i <= S.length() - T.length(); i++) {
             if (S.charAt(i) == T.charAt(0)) {
                 cnt += numDistinct(S.substring(i + 1), T.substring(1));
             }
         }
        
        return cnt;
    }
}