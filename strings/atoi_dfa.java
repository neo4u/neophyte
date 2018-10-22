// def:
// four symbols:
// 0 space
// 1 sign(+ or -)
// 2 number
// 3 others(illegal)

// five states:
// 0 initiation or only has space(one or multiple)
// 1 only has sign
// 2 only has number
// 3 has both sign and numbers
// -1 end or illegal

// and we can get state-transition matrix:
// [0,1,2,-1]
// [-1,-1,3,-1]
// [-1,-1,2,-1]
// [-1,-1,3,-1]

//     code:
class Solution {
    public int myAtoi(String str) {
        long t = 0;
        int stateMatrix[][] = { { 0, 1, 2, -1 }, { -1, -1, 3, -1 }, { -1, -1, 2, -1 }, { -1, -1, 3, -1 } };
        int l = str.length();
        int state = 0;
        int sign = 1;
        for (int i = 0; i < l; i++) {
            char c = str.charAt(i);
            if (c == ' ') {
                state = stateMatrix[state][0];
            } else if (c == '+' || c == '-') {
                if (c == '-')
                    sign = -1;
                state = stateMatrix[state][1];
            } else if (c >= '0' && c <= '9') {
                state = stateMatrix[state][2];
                t = t * 10 + c - '0';
                if (sign == 1 && t >= Integer.MAX_VALUE)
                    return Integer.MAX_VALUE;
                if (sign == -1 && t >= (long) Integer.MAX_VALUE + 1)
                    return Integer.MIN_VALUE;
            } else {
                state = stateMatrix[state][3];
            }
            if (state == -1)
                break;
        }
        return (int) (sign == 1 ? t : -t);
    }
}