public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        if (s == null)
        {
            return 0;
        }

        var set = new HashSet<char>();

        var n = s.Length;
        var left = 0;
        var right = 0;
        var ans = 0;

        while(right < n)
        {
            var c = s[right];

            if (!set.Contains(c))
            {            
                set.Add(c);  
                right++;
                ans = Math.Max(ans, right - left); 
            }
            else
            {
                set.Remove(s[left]);
                left++;       
            }
        }

        return ans;
    }
}

// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
