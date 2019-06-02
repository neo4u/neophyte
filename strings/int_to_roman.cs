public class Solution
{
    public string IntToRoman(int num)
    {
        string[] M = new string[] { "", "M", "MM", "MMM" };
        string[] C = new string[] { "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" };
        string[] X = new string[] { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" };
        string[] I = new string[] { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" };

        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10];
    }
}

// 12. Integer to Roman
// https://leetcode.com/problems/integer-to-roman/

// Approach
// 1. Using string build in. For romans and values 1000 to 1,
//    keep counting how many romans are found in num and append those many romans to result
// 2. Do a mod of that roman value to remove that order of the number and continue to smaller value
// 3. Increment i to iterate through the roman and int values

// Time: O(1), max till 12
// Space: O(1)

