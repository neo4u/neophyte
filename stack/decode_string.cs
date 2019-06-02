public class Solution
{
    public string DecodeString(string s)
    {
        var stack = new Stack<object>();
        int number = 0;

        foreach(char c in s)
        {
            if (char.IsDigit(c))
            {
                number = number * 10 + c - '0';
            }
            else if (c == '[')
            {
                stack.Push(number);
                number = 0;
            }
            else if (c == ']')
            {
                string previous = PopString(stack);
                int frequency = (int)stack.Pop();

                var sb = new StringBuilder();
                for (int j = 1; j <= frequency; j++)
                {
                    sb.Append(previous);
                }

                stack.Push(sb.ToString());
            }
            else
            {
                stack.Push(c.ToString());
            }
        }

        return PopString(stack);
    }

    private string PopString(Stack<object> stack)
    {
        var sb = new StringBuilder();

        while (stack.Any() && stack.Peek() is string)
        {
            sb.Insert(0, stack.Pop());
        }

        return sb.ToString();
    }
}