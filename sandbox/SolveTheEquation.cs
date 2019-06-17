using System;
using System.Text.RegularExpressions;

public class Solution
{
    public string SolveEquation(string equation)
    {
        var tokens = equation.Split('=');
        string left = tokens[0];
        string right = tokens[1];

        int[] leftResult = Solve(left); // EX: 2x-3 => [2,-3]
        int[] rightResult = Solve(right); //Ex: x+6 => [1,6]

        leftResult[0] -= rightResult[0];  // 2x-3 = x+6 => x = 9
        leftResult[1] = rightResult[1] - leftResult[1]; // 2x-3 = x+6 => x = 9

        if (leftResult[0] == 0 && leftResult[1] == 0) return "Infinite solutions";  //Ex: 2x+8=2x+8
        else if (leftResult[0] == 0) return "No solution";  //Ex: 2x+7=2x-4
        else return "x=" + leftResult[1] / leftResult[0]; // Ex: 2x-3 = 4x+6 => -2x = 9 => x = 9/-2
    }

    //int[0] =  number of x's
    //int[1] = sum/difference of integers
    private int[] Solve(string input)
    {
        string[] tokens = Regex.Split(input, "(?=[+-])");

        int[] result = new int[2];

        foreach (var token in tokens)
        {
            if (token == "") continue;

            if (token == "x" || token == "+x")
            {
                result[0] += 1;
            }
            else if (token == "-x")
            {
                result[0] -= 1;
            }
            else if (token.Contains("x"))
            {
                var indexOfX = token.IndexOf('x');
                var integerStr = token.Substring(0, indexOfX);
                result[0] += int.Parse(integerStr);
            }
            else
            {
                result[1] += int.Parse(token);
            }
        }

        return result;
    }
}